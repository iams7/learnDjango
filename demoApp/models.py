from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, null=False, unique=True )
    password = models.CharField(max_length=20,)#max_length=200, null= True )
