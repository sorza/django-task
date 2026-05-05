from django.db import models
from django.conf import settings

class Tarefa(models.Model):
    usuario = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                related_name= 'tarefas'
            )

    usuario = models.ForeignKey(   
        settings.AUTH_USER_MODEL,    
        on_delete = models.CASCADE,
        related_name='tarefas'
    )
    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=500, null=False, blank=False)
    data = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.titulo

