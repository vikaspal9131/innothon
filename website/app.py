from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from google.oauth2 import id_token
from google.auth.transport import requests
from google_auth_oauthlib.flow import Flow
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SECURITY_PASSWORD_SALT'] = os.getenv('SECURITY_PASSWORD_SALT')
DATABASE = 'users.db'

# Google OAuth2 configuration
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = 587
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

# Initialize the OAuth2 flow
flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'],
    redirect_uri='http://localhost:5000/google_callback'
)

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def generate_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=expiration)
    except (SignatureExpired, BadTimeSignature):
        return False
    return email

def send_verification_email(email, token):
    verification_url = url_for('verify_email', token=token, _external=True)
    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = email
    msg['Subject'] = 'Verify Your Email'

    body = f"Hello,\n\nPlease verify your email by clicking on the link below:\n{verification_url}\n\nThank you!"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(SMTP_USERNAME, email, text)
        server.quit()
        print(f"Verification email sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def role_required(roles):
    def decorator(func):
        def wrapped(*args, **kwargs):
            if 'role' not in session or session['role'] not in roles:
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('dashboard'))
            return func(*args, **kwargs)
        wrapped.__name__ = func.__name__  # Ensure function name is preserved
        return wrapped
    return decorator

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/home')
def homepage():
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'registered_user')  # Default role is 'registered_user'

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            flash('Email address already exists', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        cursor.execute("INSERT INTO users (username, email, password, role, is_verified) VALUES (?, ?, ?, ?, 0)",
                       (username, email, hashed_password, role))
        conn.commit()

        # Generate verification link (e.g., include a unique token in the URL)
        token = generate_token(email)
        send_verification_email(email, token)
        
        flash('Registration successful! Please check your email to verify your account.', 'success')
        return redirect(url_for('verify'))

    return render_template('register.html')

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('login'))

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if user and not user['is_verified']:
        cursor.execute("UPDATE users SET is_verified = 1 WHERE email = ?", (email,))
        conn.commit()
        flash('Your account has been verified!', 'success')
    else:
        flash('Account already verified or does not exist.', 'danger')

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            if user['is_verified']:
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['role'] = user['role']
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Account not verified. Please check your email.', 'warning')
                return "not verified"
        else:
            flash('Login failed. Check your email and password.', 'danger')
            return "password not match"

    return render_template('login.html')

@app.route('/google_login')
def google_login():
    authorization_url, state = flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)

@app.route('/google_callback')
def google_callback():
    flow.fetch_token(authorization_response=request.url)

    if not session['state'] == request.args['state']:
        return redirect(url_for('login'))

    credentials = flow.credentials
    request_session = requests.Request()
    userinfo = id_token.verify_oauth2_token(
        id_token=credentials.id_token, request=request_session, audience=GOOGLE_CLIENT_ID
    )

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (userinfo['email'],))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO users (username, email, is_verified) VALUES (?, ?, 1)",
                       (userinfo['name'], userinfo['email']))
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE email = ?", (userinfo['email'],))
        user = cursor.fetchone()

    session['user_id'] = user['id']
    session['username'] = user['username']
    flash('Logged in with Google successfully!', 'success')
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('You need to login first.', 'warning')
        return redirect(url_for('login'))

    user_role = session.get('role')
    return render_template('dashboard.html')

@app.route('/admin_page')
@role_required(['admin'])
def admin_page():
    return "Welcome to the admin page."

@app.route('/provider_page')
@role_required(['healthcare_provider'])
def provider_page():
    return "Welcome to the healthcare provider page."

@app.route('/user_page')
@role_required(['registered_user', 'admin', 'healthcare_provider'])
def user_page():
    return "Welcome to the user page."

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))


# Load the saved models and scalers
model_files = {
    'Logistic Regression': 'static/models/trained_model_logistic_regression.joblib',
    'SVM': 'static/models/trained_model_svm.joblib',
    'Decision Tree': 'static/models/trained_model_decision_tree.joblib',
    'Random Forest': 'static/models/trained_model_random_forest.joblib',
    'KNN': 'static/models/trained_model_knn.joblib'
}

scalers = joblib.load('static/models/scalers.joblib')
models = {name: joblib.load(filename) for name, filename in model_files.items()}

# Categorical and numerical features
categorical_features = ['Sex', 'ChestPainType', 'FastingBS', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
numerical_features = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']

# Initialize LabelEncoder for each categorical feature
encoders = {feature: LabelEncoder() for feature in categorical_features}

# Encode all the categorical features
@app.before_request
def fit_encoders():
    data = pd.read_csv('static/dataset/dataset.csv')
    for feature in categorical_features:
        encoders[feature].fit(data[feature])
        
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            data = {
                "Age": int(request.form.get('age')),
                "Sex": request.form.get('sex'),
                "ChestPainType": request.form.get('chest_pain_type'),
                "RestingBP": int(request.form.get('resting_bp')),
                "Cholesterol": int(request.form.get('cholesterol')),
                "FastingBS": int(request.form.get('fasting_bs')),
                "RestingECG": request.form.get('resting_ecg'),
                "MaxHR": int(request.form.get('max_hr')),
                "ExerciseAngina": request.form.get('exercise_angina'),
                "Oldpeak": float(request.form.get('oldpeak')),
                "ST_Slope": request.form.get('st_slope')
            }
        
            # Ensure all features are present
            for feature in categorical_features + numerical_features:
                if feature not in data:
                    flash(f"Missing feature: {feature}", 'danger')
                    return redirect(url_for('dashboard'))
            
            # Convert input data into a DataFrame
            df = pd.DataFrame([data])
            
            # Encode categorical features
            try:
                for feature in categorical_features:
                    df[feature] = encoders[feature].transform(df[feature])
            except Exception as e:
                flash(f"Error encoding feature '{feature}': {str(e)}", 'danger')
                return redirect(url_for('dashboard'))
            
            # Scale numerical features
            try:
                for feature, scaler in scalers.items():
                    df[feature] = scaler.transform(df[[feature]])
            except Exception as e:
                flash(f"Error scaling feature '{feature}': {str(e)}", 'danger')
                return redirect(url_for('dashboard'))
            
            # Predict using all models
            predictions = {}
            try:
                for name, model in models.items():
                    predictions[name] = model.predict(df).tolist()
            except Exception as e:
                flash(f"Error predicting with model '{name}': {str(e)}", 'danger')
                return redirect(url_for('dashboard'))
            
            return render_template('predict_results.html', predictions=predictions)
        
    except Exception as e:
        flash(f"General error: {str(e)}", 'danger')
        return redirect(url_for('dashboard'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<id>')
def singleBlog(id):
    return render_template('single-blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/subscription')
def subscription():
    return render_template('subscription.html')

@app.route('/forgotPassword')
def forgotPassword():
    return render_template('forgot-password.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/prediction')
def prediction():
    return render_template('upload.html')

@app.route('/prediction-analysis')
def predictionAnalysis():
    return render_template('prediction-analysis.html')

@app.route('/ecg-graph')
def ecgGraph():
    return render_template('ecg-graph.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/reports')
def report():
    return render_template('report.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        conn = get_db()
        conn.execute('''CREATE TABLE users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        password TEXT,
                        role TEXT NOT NULL DEFAULT 'registered_user',
                        is_verified INTEGER NOT NULL DEFAULT 0
                        )''')
        conn.close()
    app.run(debug=True)