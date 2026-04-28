from django.shortcuts import redirect, render
from task.forms import TarefaForm
from task.models import Tarefa
<<<<<<< HEAD
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'task/index.html')

=======
from django.contrib.auth.decorators import login_required

>>>>>>> ed35b3914545315358106ef9641a007de95ef879
@login_required
def task_list(request):
    tarefas = Tarefa.objects.all() 
    return render(request, 'task/tasks.html', {'tarefas': tarefas})

@login_required
def create_task(request):
    form = TarefaForm(request.POST or None)
<<<<<<< HEAD
    if request.method == 'POST':        
        if form.is_valid():
            form.save()
            return redirect('tasks')
    return render(request, 'task/create_task.html', {'form': form})
=======
    if request.method == 'POST': 
        if form.is_valid():
            form.save()            
        return redirect('tasks')    
    return render(request, 'task/create_task.html', {'tarefa':form})
>>>>>>> ed35b3914545315358106ef9641a007de95ef879

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
<<<<<<< HEAD
    form = TarefaForm(request.POST or None, instance=tarefa)
    if request.method == 'POST':       
        if form.is_valid():
            form.save()
            return redirect('tasks')
    
    return render(request, 'task/update_task.html', {'task': tarefa, 'form': form})
=======
    form = TarefaForm(request.POST or None, instance=tarefa)    
    if request.method == 'POST':
        if form.is_valid():
            tarefa.save()
            return redirect('tasks')  
        return render(request, 'task/update_task.html', {'task': tarefa,'tarefa':form})  
    return render(request, 'task/update_task.html',{'task': tarefa})
>>>>>>> ed35b3914545315358106ef9641a007de95ef879
