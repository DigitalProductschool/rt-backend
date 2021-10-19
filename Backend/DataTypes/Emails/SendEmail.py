from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_email(config_email, dps_email, dps_password, email):
    msg = MIMEMultipart()
    msg_template = config_email
    msg['Subject'] = msg_template["subject"]
    msg['From'] = f"DPS Applications{dps_email}"
    msg['To'] = email
    body = MIMEText(msg_template["body"], 'html')
    msg.attach(body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(dps_email, dps_password)
        smtp.send_message(msg)
