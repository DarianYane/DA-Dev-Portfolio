from django.contrib import admin

# Register your models here.
from .models import Job, Department

# Register your models here.
admin.site.register(Job)
admin.site.register(Department)