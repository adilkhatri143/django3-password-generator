from django.shortcuts import render
import random
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 10))

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))
    
    if request.GET.get('special'):
        character.extend(list('!@#$%^&'))

    generated_password = ''

    for x in range(length):
        generated_password += random.choice(character)
    
    context = {
        'password' : generated_password,
    }
    return render(request, 'generator/password.html',context)