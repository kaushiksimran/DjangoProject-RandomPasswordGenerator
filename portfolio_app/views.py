from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'portfolio_app/about.html')

def pwd_gen(request):
    a=int(request.GET.get('uppercase'))
    b=int(request.GET.get('lowercase'))
    c=int(request.GET.get('digits'))
    d=int(request.GET.get('special'))

    upper= list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower= list('abcdefghijklmnopqrstuvwxyz')
    digit=list('0123456789')
    special=list('!@#$%^&*')

    password_list=[]

    for i in range(0,a+1):
        password_list+=random.choice(upper)
    for i in range(0,b+1):
        password_list+=random.choice(lower)
    for i in range(0,c+1):
        password_list+=random.choice(digit)
    for i in range(0,d+1):
        password_list+=random.choice(special)

    random.shuffle(password_list)
    password=""

    for i in password_list:
        password+=i

    print(password)

    return render(request, 'portfolio_app/password_generator.html',{'result':password})
