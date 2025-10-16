from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length= 30, null= True, blank= True)
    last_name = models.CharField(max_length= 30, null= False)
    email = models.EmailField(max_length= 30, blank= True)
    age = models.IntegerField()
    details = models.TextField()