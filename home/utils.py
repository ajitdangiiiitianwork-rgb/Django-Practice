from home.models import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import time

def run_this_fun():
  print("Function started")
  time.sleep(2)
  print("Function executed")

def send_mail_to_client():
  subject = "This is test mail from Django"
  message = "This is a test message from Django server mail...😉"
  from_email = settings.EMAIL_HOST_USER
  recipient_list = ["112415014@cse.iiitp.ac.in"]
  send_mail(subject, message, from_email, recipient_list)

def send_mail_with_attachment(subject, message, recipient_list, file_path):
  mail = EmailMessage(subject = subject, body=message, from_email=settings.EMAIL_HOST_USER, to = recipient_list)
  mail.attach_file(file_path)
  mail.send()
