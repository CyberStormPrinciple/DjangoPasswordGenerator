from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    password = ''

    characters = list('abcdefghijklkmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # Defaults to 12 length if no stated params given
    length = int(request.GET.get('length', '12'))

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})
