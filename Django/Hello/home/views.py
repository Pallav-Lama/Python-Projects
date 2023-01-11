from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import ToDoList
# from django.contrib.messages import constants as messages
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def todolist(request):
    return dataset(request)
def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("contact")
        desc = request.POST.get("query")
        date = datetime.today()
        contact = Contact(name=name, email=email, phone=phone,desc=desc, date=date)
        contact.save()
        messages.success(request, 'Your request has been recieved.')
        
    return render(request, 'contact.html')

def add(request):
    if request.method=="POST":
        titleName = request.POST.get("titleName")
        todolist = ToDoList(titleName=titleName)
        todolist.save()
        messages.success(request, 'Title Added Successfully.')
    return dataset(request)

def search(request):
    if request.method=="POST":
        titleName = request.POST.get("titleName")
    lists={}
    lists["dataset"] = ToDoList.objects.filter(titleName = titleName)
    return render(request, 'todolist.html', lists)


def delete(request, titleName):
    if request.method != "POST":
        return render(request, 'delete.html')
    else:
        todolist = ToDoList.objects.get(titleName = titleName)
        todolist.delete()
        messages.success(request, 'Title Deleted Successfully.')
        return dataset(request)

def dataset(request):
    lists={}
    lists["dataset"] = ToDoList.objects.all()
    return render(request, 'todolist.html', lists)