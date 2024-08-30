from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from .auth import generate_token, confirm_token, send_verification_email, role_required
from .models import get_db
from .prediction import predict
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import sqlite3
import requests
import scipy.io

bp = Blueprint('main', __name__)

# Path to the upload folder
uploads_folder = 'uploads'
os.makedirs(uploads_folder, exist_ok=True)

@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/home')
def homepage():
    return render_template('homepage.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'registered_user')

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            flash('Email address already exists', 'danger')
            return redirect(url_for('main.register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        cursor.execute("INSERT INTO users (username, email, password, role, is_verified) VALUES (?, ?, ?, ?, 0)",
                       (username, email, hashed_password, role))
        conn.commit()

        token = generate_token(email)
        send_verification_email(email, token)
        
        flash('Registration successful! Please check your email to verify your account.', 'success')
        return redirect(url_for('main.verify'))

    return render_template('register.html')

@bp.route('/verify')
def verify():
    return render_template('verify.html')

@bp.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    email = confirm_token(token)
    if not email:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('main.login'))

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

    return redirect(url_for('main.login'))

@bp.route('/login', methods=['GET', 'POST'])
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
                return redirect('http://localhost:8501/')
            else:
                flash('Account not verified. Please check your email.', 'warning')
                return "not verified"
        else:
            flash('Login failed. Check your email and password.', 'danger')
            return "password not match"

    return render_template('login.html')

@bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('You need to login first.', 'warning')
        return redirect(url_for('main.login'))

    return render_template('dashboard.html')

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('main.login'))

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/blog')
def blog():
    return render_template('blog.html')

@bp.route('/blog/<id>')
def single_blog(id):
    return render_template('single-blog.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/services')
def services():
    return render_template('services.html')

@bp.route('/subscription')
def subscription():
    return render_template('subscription.html')

@bp.route('/forgotPassword')
def forgot_password():
    return render_template('forgot-password.html')


@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get user information
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        ecg_option = request.form.get('ecg-option')
        selected_ecg = request.form.get('ecg-select')
        drive_link = request.form.get('google-drive-link')
        # Handle file upload
        if ecg_option == 'upload' and 'file-input' in request.files:
            file = request.files['file-input']
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(uploads_folder, filename)
                file.save(file_path)

                # Save file info to database
                conn = get_db_connection()
                conn.execute('INSERT INTO uploads (name, age, gender, file_path) VALUES (?, ?, ?, ?)',
                             (name, age, gender, file_path))
                conn.commit()
                conn.close()

                return redirect(url_for('main.upload'))
        elif ecg_option == 'existing' and selected_ecg:
            # [google drive download is not working]
            download_file_from_google_drive(drive_link, uploads_folder)
                # Handle existing ECG selection
            conn = get_db_connection()
            conn.execute('INSERT INTO uploads (name, age, gender, selected_ecg) VALUES (?, ?, ?, ?)',
                            (name, age, gender, selected_ecg))
            conn.commit()
            conn.close()
            return redirect(url_for('main.upload'))

            
        elif ecg_option == 'drive' and drive_link:
            # Handle Google Drive link
            conn = get_db_connection()
            conn.execute('INSERT INTO uploads (name, age, gender, drive_link) VALUES (?, ?, ?, ?)',
                         (name, age, gender, drive_link))
            conn.commit()
            conn.close()

            return redirect(url_for('main.upload'))

    return render_template('upload.html')

@bp.route('/prediction')
def prediction():
    return render_template('upload.html')

@bp.route('/prediction-analysis')
def prediction_analysis():
    return render_template('prediction-analysis.html')

@bp.route('/ecg-graph')
def ecg_graph():
    return render_template('ecg-graph.html')

@bp.route('/base')
def base():
    return render_template('base.html')

@bp.route('/reports')
def report():
    return render_template('report.html')

@bp.route('/documentation')
def documentation():
    return render_template('documentation.html')

@bp.route('/faq')
def faq():
    return render_template('faq.html')

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@bp.route('/list_files', methods=['GET'])
def list_files():  # Update this path to your uploads directory
    files=os.listdir(uploads_folder)
    return jsonify({'files': files})


def download_file_from_google_drive(url, destination):
    """Download a file from Google Drive and save it to the specified destination."""
    
    session = requests.Session()
    response = session.get(url, stream=True)
    print('res', response)
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

@bp.route('/ecg-data/<filename>', methods=['GET'])
def get_ecg_data(filename):
    file_path = uploads_folder + '/' + filename
    
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        mat_data = scipy.io.loadmat(file_path)
        ecg_data = mat_data['val']
        
        if ecg_data.size == 0:
            return jsonify({'error': 'No ECG data found'}), 404
        
        # Select a specific row (e.g., the first row) or process as needed
        ecg_data = ecg_data[0].flatten().tolist()
        
        print(f"ECG Data: {ecg_data[:10]}...")  # Log the first 10 data points
        return jsonify({'ecg_signal': ecg_data})
    
    except Exception as e:
        print(f"Error: {str(e)}")  # Log the error
        return jsonify({'error': 'Internal server error'}), 500
