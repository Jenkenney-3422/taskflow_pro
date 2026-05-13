from django.shortcuts import render, redirect
from .models import Task
from .tasks import process_task_data

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        # Save to Postgres
        new_task = Task.objects.create(title=title)
        
        # Trigger Celery background job
        process_task_data.delay(new_task.id)
        
        return redirect('task_list')
    return render(request, 'tasks/create.html')