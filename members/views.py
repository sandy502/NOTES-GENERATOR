from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.
# Django views are Python functions that takes http requests and returns http response, like HTML documents.

def index(request):
    template = loader.get_template('index.html')
    mymember = Members.objects.all().values()
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firsname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))  

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index')) 

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))   

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firsname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))
