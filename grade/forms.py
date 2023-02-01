from django.forms import ModelForm
from .models import Student, Rating

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': ('Enter the name of the student you want to register')
        }

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'