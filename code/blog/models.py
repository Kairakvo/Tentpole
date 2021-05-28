from typing import ContextManager
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    firstname = models.CharField(max_length=155)
    lastname = models.CharField(max_length=155,default="noname")
    dob = models.DateField(default=timezone.now)
    file = models.FileField(default=False)
    
    def __str__(self):
        return self.firstname
class Customer(models.Model):
    firstname = models.CharField(max_length=155)
    lastname = models.CharField(max_length=155)
    dob = models.DateField()
    file = models.FileField(upload_to="media")

    def __str__(self):
        return self.firstname
