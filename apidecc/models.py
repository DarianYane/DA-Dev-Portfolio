from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=200, unique = True)
    
    def __str__(self):
        return self.department

class Job(models.Model):
    job = models.CharField(max_length=100, unique = True)
    
    def __str__(self):
        return self.job

class HiredEmployee(models.Model):
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    department_id = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    job_id = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)