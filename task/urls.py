from django.urls import include, path
from .views import index, task_list,create_task,delete_task,update_task

urlpatterns = [
    path('', task_list, name='tasks'),   
    path('create/', create_task, name='create'),
    path('delete/<int:id>/', delete_task, name='delete'),
    path('edit/<int:id>/', update_task, name='edit'),
    path('accounts/', include('django.contrib.auth.urls')),
]
