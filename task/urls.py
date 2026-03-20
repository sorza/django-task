from django.urls import path
from .views import index, task_list

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', task_list, name='tasks'),
]
