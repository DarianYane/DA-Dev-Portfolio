from django.contrib import admin

# Register your models here.
from .models import Job, Department, HiredEmployee

# Register your models here.
admin.site.register(Job)
admin.site.register(Department)
admin.site.register(HiredEmployee)