from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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