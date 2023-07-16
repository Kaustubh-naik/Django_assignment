from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('createTask/', CreateTodoTaskView.as_view(), name='createTask'),
    path('editTask/<uuid:task_id>/', edit_todo_task, name='edit_todo_task'),
    path('deleteTask/<uuid:task_id>/', delete_todo_task, name='delete_todo_task'),
]
