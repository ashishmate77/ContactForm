from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=30)
    salary = models.IntegerField()
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    location = models.CharField(max_length=50)