from django.shortcuts import render

def index(request):
    return render(request, 'task/index.html')

def task_list(request):
    return render(request, 'task/tasks.html')