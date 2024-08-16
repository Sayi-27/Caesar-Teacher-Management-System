from django.db import models

# Create your models here.
class Teacher(models.Model):
    TSC_Number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Rensponsibility = models.CharField(max_length=50)
    Subject = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField()
    
    def __str__(self):
        return f'Teacher: {self.first_name} {self.last_name}'