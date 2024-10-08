from app import mail
from flask_mail import Message
from flask import current_app
from threading import Thread


def async_send_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, recipients, text_body, html_body):
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=async_send_email,
           args=(current_app._get_current_object(), msg)).start()
