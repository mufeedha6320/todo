from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from todoapp.forms import TodoForm
from todoapp.models import Task

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'key1'

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk': self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'keyname'
    success_url = reverse_lazy('cbvhome')
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'taskObj'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'key1'
    fields = ('name', 'priority', 'date')


    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})

'''
def home(request):
    #get all tasks
    my_tasks = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date','')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, "home.html", {'key1': my_tasks})
def delete(request,id):
    task = Task.objects.get(id=id)
    name = Task.objects.get(name=task)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html', {'keyname': name})
def update(request,id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
'''

