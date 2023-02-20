from django.forms import ModelForm
from .models import Student, Rating

#Form to create a new student through modelform
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': ('Enter the name of the student you want to register')
        }

#Form to create a new rating through modelform
class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'