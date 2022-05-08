from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import Taskform

# Create your views here.


def indextask(request):
    tasks = Tasktodo.objects.all()

    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Tasktodo.objects.get(id=pk)

    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'tasks/update.html', context)    


def deleteTask(request, pk):
    item = Tasktodo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)