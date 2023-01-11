from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("todolist", views.todolist, name='todolist'),
    path("contact", views.contact, name='contact'),
    path("add", views.add, name='add'),
    path("search", views.search, name='search'),
    path("delete/<str:titleName>/", views.delete, name='delete')
]