from django.db import models

# Create your models here.
#Task list for the roadmap
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField(verbose_name='Year expected to be completed:', default=2022)
    is_completed = models.BooleanField(default=False, verbose_name='Has this task been completed?')

    def __str__(self):
        return self.title
