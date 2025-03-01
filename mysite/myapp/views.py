from django.shortcuts import redirect, render
from .models import Task
from .forms import ToDoForm
from django.views.generic import ListView
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'myapp/index.html'
    context_object_name = 'task_list'

def index(request):
    task_list = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date = date)
        task.save()
        return redirect('/')
    return render(request,'myapp/index.html',{'task_list':task_list})

def delete(request,taskid):
    task = Task.objects.get(id = taskid)
    if request.method =="POST":
        task.delete()
        return redirect('/')
    return render(request,'myapp/delete.html',{'task':task})

def edit(request,id):
    task = Task.objects.get(id=id)
    form = ToDoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/edit.html',{'form':form,'task':task})
