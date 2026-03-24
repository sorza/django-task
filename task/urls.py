from django.urls import path
from .views import index, task_list,create_task

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', task_list, name='tasks'),
    path('create/', create_task, name='create'),
]
