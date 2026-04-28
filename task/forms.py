from django import forms
<<<<<<< HEAD
from .models import Tarefa
=======
from task.models import Tarefa
>>>>>>> ed35b3914545315358106ef9641a007de95ef879

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
<<<<<<< HEAD
        fields = ['titulo', 'descricao', 'data', 'status']
    
=======
        fields = ['titulo', 'descricao','data','status']
        
        

>>>>>>> ed35b3914545315358106ef9641a007de95ef879
