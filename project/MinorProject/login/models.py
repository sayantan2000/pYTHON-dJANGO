from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=21)