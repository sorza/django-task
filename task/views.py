from django.shortcuts import redirect, render
from task.forms import TarefaForm
from task.models import Tarefa

def index(request):
    return render(request, 'task/index.html')

def task_list(request):
    tarefas = Tarefa.objects.all() 
    return render(request, 'task/tasks.html', {'tarefas': tarefas})

def create_task(request):
    form = TarefaForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()            
        return redirect('tasks')    
    return render(request, 'task/create_task.html', {'tarefa':form})

def delete_task(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tasks')
    
    return render(request, 'task/delete_task.html', {'task': tarefa})

def update_task(request, id):
    tarefa = Tarefa.objects.get(id=id)
    form = TarefaForm(request.POST or None)    
    if request.method == 'POST':
        if form.is_valid():            
            tarefa.titulo = request.POST.get('titulo')
            tarefa.descricao = request.POST.get('descricao')
            tarefa.data = request.POST.get('data')
            tarefa.status = 'status' in request.POST
            tarefa.save()
            return redirect('tasks')  
        return render(request, 'task/update_task.html', {'task': tarefa,'tarefa':form})  
    return render(request, 'task/update_task.html',{'task': tarefa})