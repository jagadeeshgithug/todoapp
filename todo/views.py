from django.shortcuts import render , redirect

from .models import todomodel
from .form import todoform
# Create your views here.

def todoview(request):

    form=todoform()
    todos=todomodel.objects.all()

    context={
        'todos':todos,
        'form':form
    }
    return render(request,'todo/todo.html',context)

def todoaddview(request):
    if request.method=='POST':
        form=todoform(request.POST)
        if form.is_valid():
            new_todo=todomodel(text=request.POST['text'])
            new_todo.save()
    return redirect('/')

def tododelete(request,todo_id):
    todomodel.objects.filter(pk=todo_id).delete()

    return redirect('/')