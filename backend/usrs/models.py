from django.db import models

# Create your models here.
class Usr(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254,unique=True)
    idname = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)