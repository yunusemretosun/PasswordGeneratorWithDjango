from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')
    
def password(request):

    thepassword = ''
    length = int(request.GET.get('length'),12)
    characaters = list('abcdefghijklmnoprstyuvyz')

    if request.GET.get('uppercase'):
        characaters.extend(list('ABCDEFGHJIKLMNOPRSUTVWXYZ'))
    
    if request.GET.get('special'):
        characaters.extend(list('!.@&/=?_-#*'))

    if request.GET.get('numbers'):
        characaters.extend(list('1234567890'))

    for i in range(length):
        thepassword += random.choice(characaters)
        
    return render(request,'generator/password.html',{'generatedPassword':thepassword})