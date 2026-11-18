from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    #model-Database structure
    #views-Application logic
    #Templet-Html user interface
    #URL-connects gthe browser requests to viewss