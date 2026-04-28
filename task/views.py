from django.shortcuts import redirect, render
from task.forms import TarefaForm
from task.models import Tarefa
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'task/index.html')

@login_required
def task_list(request):
    tarefas = Tarefa.objects.all() 
    return render(request, 'task/tasks.html', {'tarefas': tarefas})

def create_task(request):
    form = TarefaForm(request.POST or None)
    if request.method == 'POST':        
        if form.is_valid():
            form.save()
            return redirect('tasks')
    return render(request, 'task/create_task.html', {'form': form})

def delete_task(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tasks')
    
    return render(request, 'task/delete_task.html', {'task': tarefa})

def update_task(request, id):
    tarefa = Tarefa.objects.get(id=id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if request.method == 'POST':       
        if form.is_valid():
            form.save()
            return redirect('tasks')
    
    return render(request, 'task/update_task.html', {'task': tarefa, 'form': form})
