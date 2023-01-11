from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class ToDoList(models.Model):
    titleName = models.CharField(max_length=60)

