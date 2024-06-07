import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import current_app

def send_email(recipient, subject, body, html=False):
    sender_email = current_app.config['MAIL_USERNAME']
    sender_password = current_app.config['MAIL_PASSWORD']
    smtp_server = current_app.config['MAIL_SERVER']
    smtp_port = current_app.config['MAIL_PORT']

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient
    message['Subject'] = subject

    if html:
        message.attach(MIMEText(body, 'html'))
    else:
        message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
        return True
    except Exception as e:
        current_app.logger.error(f"Error sending email: {e}")
        return False

def send_confirmation_email(email, homepage_url):
    body = f'''
    Thank you for registering!
    Please click the following link to confirm your registration:
    {homepage_url}
    '''
    return send_email(email, 'Registration Confirmation', body)

def send_password_reset_email(email, reset_link):
    body = f'''
    You have requested to reset your password.
    Please click the following link to reset your password:
    {reset_link}
    '''
    return send_email(email, 'Password Reset Request', body, html=True)
