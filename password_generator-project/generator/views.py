from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    generated_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',8))   #default value 8

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    for x in range(length):
        generated_password += random.choice(characters)

    return render(request,'generator/password.html',{'password':generated_password})

def about(request):
    return render(request,'generator/about.html')