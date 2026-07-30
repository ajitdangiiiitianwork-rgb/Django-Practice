from django.shortcuts import redirect, render
from django.http import HttpResponse
from .utils import send_mail_to_client, send_mail_with_attachment
from django.conf import settings

# Create your views here.
def send_email(request):
  subject = "This mail is from Django server."
  message = "Please check the attached document."
  recipient_list = ['112415014@cse.iiitp.ac.in']
  path = f"{settings.BASE_DIR}/home/templates/home/index.html"
  send_mail_with_attachment(subject=subject, message=message, recipient_list=recipient_list, file_path=path)
  return redirect('/')

def home(request):
  people = [
    {'name' : 'Ajit', 'age' : 21},
    {'name' : 'Rishbah', 'age' : 24},
    {'name' : 'Ayush', 'age': 31},
    {'name' : 'Shubham', 'age': 28},
    {'name' : 'Siddharth', 'age': 27},
  ]


  return render(request, 'home/index.html', context= {'peoples' : people})

def contact(request):
  return render(request, 'home/contact.html')

def about(request):
  return render(request, 'home/about.html')