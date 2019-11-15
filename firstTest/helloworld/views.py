from django.shortcuts import render
import requests
import json
from .models import Contact

# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse('<h1>Hello World!</h1>')

def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data['value']['joke']

        context = {'joker': joke}
        return render(request, 'helloworld/index.html', context)
    else:
        return render(request, 'helloworld/index.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = Contact(email = email, subject = subject, message = message)
        c.save()
        return render(request, 'helloworld/thank.html')
    else:
        return render(request, 'helloworld/contact.html')

def portfolio(request):
    return render(request, 'helloworld/portfolio.html')