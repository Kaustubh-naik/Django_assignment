from django.urls import path
from .views import *

urlpatterns = [
    path('', login_page, name='login_page'),
    path('home/', todo_list, name='todo_list'),
    path('pending/', show_pending_task,name='show_pending_task'),
    path('createTask/', CreateTodoTaskView.as_view(), name='createTask'),
    path('editTask/<uuid:task_id>/', edit_todo_task, name='edit_todo_task'),
    path('deleteTask/<uuid:task_id>/', delete_todo_task, name='delete_todo_task'),
    path('logout/', logout_view, name='logout_view'),
    
]
