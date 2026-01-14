import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv("info.env")
email = os.getenv("EMAIL")
emailPassword = os.getenv("EMAIL_PASSWORD")

def email_alert(subject, body, to):
  msg = EmailMessage()
  msg.set_content(body)
  msg['subject'] = subject
  msg['to'] = to
  msg['from'] = email
  
  # Connect to SMTP server
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(email, emailPassword)
  server.send_message(msg)
  server.quit()






