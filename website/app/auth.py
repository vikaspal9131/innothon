from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app
from app.models import get_db
from functools import wraps

bp = Blueprint('auth', __name__)

def generate_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt=current_app.config['SECURITY_PASSWORD_SALT'], max_age=expiration)
    except (SignatureExpired, BadTimeSignature):
        return False
    return email

def send_verification_email(email, token):
    verification_url = url_for('auth.verify_email', token=token, _external=True)
    msg = MIMEMultipart()
    msg['From'] = current_app.config['SMTP_USERNAME']
    msg['To'] = email
    msg['Subject'] = 'Email Verification'
    body = f'Please click the following link to verify your email: {verification_url}'
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(current_app.config['SMTP_SERVER'], current_app.config['SMTP_PORT']) as server:
        server.starttls()
        server.login(current_app.config['SMTP_USERNAME'], current_app.config['SMTP_PASSWORD'])
        server.send_message(msg)

def role_required(role):
    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if 'role' not in session or session['role'] != role:
                flash('You do not have permission to access this page.', 'warning')
                return redirect(url_for('auth.login'))
            return func(*args, **kwargs)
        return decorated_function
    return wrapper

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
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        cursor.execute("INSERT INTO users (username, email, password, role, is_verified) VALUES (?, ?, ?, ?, 0)",
                       (username, email, hashed_password, role))
        conn.commit()

        token = generate_token(email)
        send_verification_email(email, token)
        
        flash('Registration successful! Please check your email to verify your account.', 'success')
        return redirect(url_for('auth.verify'))

    return render_template('register.html')

@bp.route('/verify')
def verify():
    return render_template('verify.html')

@bp.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    email = confirm_token(token)
    if not email:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('auth.login'))

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

    return redirect(url_for('auth.login'))

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
                return redirect(url_for('main.dashboard'))
            else:
                flash('Account not verified. Please check your email.', 'warning')
                return "not verified"
        else:
            flash('Login failed. Check your email and password.', 'danger')
            return "password not match"

    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.login'))
