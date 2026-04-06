from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from .models import Task, Priority, Category

@login_required
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    priorities = Priority.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            deadline=request.POST['deadline'],
            status=request.POST['status'],
            priority_id=request.POST.get('priority') or None,
            category_id=request.POST.get('category') or None,
        )
        return redirect('/')
    return render(request, 'tasks/task_form.html', {
        'priorities': priorities,
        'categories': categories,
        'form': Task(),
    })

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    priorities = Priority.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.deadline = request.POST['deadline']
        task.status = request.POST['status']
        task.priority_id = request.POST.get('priority') or None
        task.category_id = request.POST.get('category') or None
        task.save()
        return redirect('/')
    return render(request, 'tasks/task_form.html', {
        'form': task,
        'priorities': priorities,
        'categories': categories,
    })

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def offline(request):
    return render(request, 'tasks/offline.html')