from django.contrib import admin

# Register your models here.
from .models import Student, Course, Commission, Tasks_to_Evaluate, Terms_of_Delivery, Rating

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Commission)
admin.site.register(Tasks_to_Evaluate)
admin.site.register(Terms_of_Delivery)
admin.site.register(Rating)