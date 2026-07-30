from django.shortcuts import redirect, render
from django.http import HttpResponse
from .utils import send_mail_to_client

# Create your views here.
def send_email(request):
  send_mail_to_client()
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