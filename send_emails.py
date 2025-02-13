import os
from dotenv import load_dotenv
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib

load_dotenv()

# HTML file path
FILE_PATH = Path(__file__).parent / 'index.html'

# Sender's and recipient's information
sender = os.getenv('FROM_EMAIL', '')
recipient = "example@gmail.com"

# SMTP settings
smtp_server = os.getenv('SMTP_SERVER', '')
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')


def create_and_send_emails(product_name: str, product_url: str) -> str:

    # Text message
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        text_file = file.read()
        template = Template(text_file)
        text_email = template.substitute(product=product_name, url=product_url)

    # Converting the message to MimeMultipart
    mime_multipart = MIMEMultipart()
    mime_multipart['from'] = sender
    mime_multipart['to'] = recipient
    mime_multipart['subject'] = 'Price Drop Alert – The Product'\
        'You’re Monitoring Just Got Cheaper!'

    corpo_email = MIMEText(text_email, 'html', 'utf8')
    mime_multipart.attach(corpo_email)

    # Starting Connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(mime_multipart)

    return 'E-mail sent successfully'
