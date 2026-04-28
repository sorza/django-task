from django.urls import include, path
<<<<<<< HEAD
from .views import index, task_list,create_task,delete_task,update_task

urlpatterns = [
    path('', task_list, name='tasks'),   
=======
from .views import task_list,create_task,delete_task,update_task

urlpatterns = [
    path('', task_list, name='index'),    
>>>>>>> ed35b3914545315358106ef9641a007de95ef879
    path('create/', create_task, name='create'),
    path('delete/<int:id>/', delete_task, name='delete'),
    path('edit/<int:id>/', update_task, name='edit'),
    path('accounts/', include('django.contrib.auth.urls')),
]
