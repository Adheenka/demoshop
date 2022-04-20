from django.shortcuts import render, redirect
from . models import Task

# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        task=Task(name=name,priority=priority)
        task.save()

    return render(request,'home.html',{'task1':task1})
#def details(request):

#    return render(request,'detail.html')
#delete code
def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
       task.delete()
       return redirect('/')
    return render(request,'delete.html')
