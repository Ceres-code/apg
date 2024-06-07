from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.models import User
from app.services.email import send_password_reset_email, send_confirmation_email
import secrets
from app.extensions import db 

auth_bp = Blueprint('auth', __name__)

def generate_reset_token():
    return secrets.token_urlsafe(20)

@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.query.filter_by(reset_token=token).first()
    if not user:
        flash('Invalid or expired token', 'warning')
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        user.password_hash = hashed_password
        user.reset_token = None
        db.session.commit()
        flash('Your password has been reset', 'success')
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(username=request.form['username']).first()
    if user and check_password_hash(user.password_hash, request.form['password']):
        login_user(user)
        return redirect(url_for('movies.homepage'))
    else:
        flash('Invalid username or password')
        return redirect(url_for('auth.signin'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.signin'))

@auth_bp.route('/reset_password_request', methods=['POST', 'GET'])
def reset_password_request():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            token = generate_reset_token()
            reset_link = url_for('auth.reset_password', token=token, _external=True)
            user.reset_token = token
            db.session.commit()
            send_password_reset_email(email, reset_link)
            flash('Reset password email has been sent. Please check your spam folder.')
            return render_template('signin.html')        
        else:
            return 'No user found with that email address.'
    return render_template('reset_password_request.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not (username and email and password):
            return 'Error: All fields are required.'

        new_user = User(username=username, email=email, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()

            homepage_url = 'https://alien-playground.com'  
            send_confirmation_email(email, homepage_url)

            flash('You are now registered', 'success')
            return redirect(url_for('auth.signin'))
        except Exception as e:
            print("An error occurred:", e)
            return 'Error: Registration failed.'
    else:
        return render_template('register.html')

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('movies.homepage'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('auth.signin'))
    else:
        return render_template('signin.html')
