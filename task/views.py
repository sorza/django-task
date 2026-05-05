from django.shortcuts import redirect, render
from task.forms import TarefaForm
from task.models import Tarefa
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tarefas = Tarefa.objects.filter(usuario = request.user) 
    #tarefas = request.user.tarefas.all()
    return render(request, 'task/tasks.html', {'tarefas': tarefas})

@login_required
def create_task(request):
    form = TarefaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        tarefa = form.save(commit = False)
        tarefa.usuario = request.user
        tarefa.save()           
        return redirect('index')    
    return render(request, 'task/create_task.html', {'tarefa':form})

@login_required
def delete_task(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tasks')    
    return render(request, 'task/delete_task.html', {'task': tarefa})

@login_required
def update_task(request, id):
    tarefa = Tarefa.objects.get(id=id)
    form = TarefaForm(request.POST or None, instance=tarefa)    
    if request.method == 'POST':
        if form.is_valid():
            tarefa.save()
            return redirect('tasks')  
        return render(request, 'task/update_task.html', {'task': tarefa,'tarefa':form})  
    return render(request, 'task/update_task.html',{'task': tarefa})