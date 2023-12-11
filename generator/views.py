from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def generate_random_string(length,uppercase,special):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def easter(request):
    return render(request, 'generator/easter.html')

def password(request):
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    special = request.GET.get('special')
    uppercase_bool = True if uppercase == 'on' else False
    special_bool = True if special == 'on' else False
    password = generate_random_string(length, uppercase_bool, special_bool)
    return render(request, 'generator/password.html' ,  {'password' : password})