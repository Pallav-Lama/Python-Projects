from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=90)
    contact = models.CharField(max_length=60)
    doj = models.DateField()
    department = models.CharField(max_length=60)
    email = models.EmailField()