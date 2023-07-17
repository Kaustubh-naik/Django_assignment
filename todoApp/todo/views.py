from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import TodoTask
from django.views import View
from .forms import TodoTaskForm

def todo_list(request):
    tasks = TodoTask.objects.all()
    return render(request, 'html/homePage.html', {'tasks': tasks})

def show_pending_task(request):
    incomplete_tasks = TodoTask.objects.filter(is_completed=False)
    return render(request, 'html/homePage.html', {'tasks': incomplete_tasks})

class CreateTodoTaskView(View):
    def get(self, request):
        form = TodoTaskForm()
        return render(request, 'html/createTodoTask.html', {'form': form})

    def post(self, request):
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            user = form.cleaned_data['user']
            is_completed = form.cleaned_data['is_completed']
            todo_task = TodoTask(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                user=user,
                is_completed=is_completed
            )
            todo_task.save()
            messages.success(request, 'Todo task created successfully.')
            return redirect('todo_list')
        return render(request, 'html/createTodoTask.html', {'form': form})

def edit_todo_task(request, task_id):
    task = get_object_or_404(TodoTask, id=task_id)

    if request.method == 'POST':
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.start_date = form.cleaned_data['start_date']
            task.end_date = form.cleaned_data['end_date']
            task.user = form.cleaned_data['user']
            task.is_completed = form.cleaned_data['is_completed']
            task.save()
            messages.success(request, 'Todo task edited successfully.')
            return redirect('todo_list')  # Redirect to the desired page after successful editing
    else:
        form = TodoTaskForm(initial={
            'title': task.title,
            'description': task.description,
            'start_date': task.start_date,
            'end_date': task.end_date,
            'user': task.user,
            'is_completed': task.is_completed
        })
    
    return render(request, 'html/editTodoTask.html', {'form': form})

def delete_todo_task(request, task_id):
    task = get_object_or_404(TodoTask, id=task_id)
    task.delete()
    messages.error(request, 'Todo task deleted successfully.')
    return redirect('todo_list')

