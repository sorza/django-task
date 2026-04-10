from django.urls import path
from .views import index, task_list,create_task,delete_task,update_task

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', task_list, name='tasks'),
    path('create/', create_task, name='create'),
    path('delete/<int:id>/', delete_task, name='delete'),
    path('edit/<int:id>/', update_task, name='edit'),
]
