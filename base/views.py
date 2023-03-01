from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Task, Topic
from .forms import TaskForm

def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    tasks = Task.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Topic.objects.all()
    task_count = tasks.count()

    context = {'tasks':tasks, 'topics':topics, 'task_count':task_count}
    return render(request, 'base/home.html', context)

def task(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}

    return render(request, 'base/task.html', context)

def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/task_form.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/task_form.html', context )

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':task})