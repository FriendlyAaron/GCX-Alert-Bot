import smtplib
import os
from email.message import EmailMessage

def email_alert(subject, body, to):
  msg = EmailMessage()
  msg.set_content(body)
  msg['subject'] = subject
  msg['to'] = to
  email =os.environ ['email']
  emailPassword =os.environ ['emailPassword']
  msg['from'] = email
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(email, emailPassword)
  server.send_message(msg)
  server.quit()






