from django.shortcuts import render, HttpResponse
from datetime import datetime
from blog.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('this is home page.')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('this is about page.')

def write(request):
    return render(request, 'write.html')
    # return HttpResponse('this is create blog page.')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')
        state = request.POST.get('state')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, password=password, city=city, state=state, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Congratulations!!! We have recieved your message. :)')
    return render(request, 'contact.html')
    # return HttpResponse('this is contact page.')            