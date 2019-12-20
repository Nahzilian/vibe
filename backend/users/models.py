from django.db import models
from django import forms

class User(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField(max_length=150,unique=True)
    idname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.TimeField(auto_now_add=True)


