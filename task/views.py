from django.shortcuts import redirect, render
from task.models import Tarefa

def index(request):
    return render(request, 'task/index.html')

def task_list(request):
    tarefas = Tarefa.objects.all() 
    return render(request, 'task/tasks.html', {'tarefas': tarefas})

def create_task(request):
    if request.method == 'POST': 
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        status = False
        Tarefa.objects.create(titulo = titulo, descricao = descricao, data = data, status = status)
        return redirect('tasks')
    
    return render(request, 'task/create_task.html')