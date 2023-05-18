from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=200)
    
    def __str__(self):
        return self.department

class Job(models.Model):
    job = models.CharField(max_length=100)
    
    def __str__(self):
        return self.job