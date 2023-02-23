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

#Form to update a rating
class UpdateRatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('student', 'terms_of_delivery', 'URL_delivery', 'criteria_01_score', 'criteria_02_score', 'criteria_03_score', 'criteria_04_score', 'total_score', 'rating', 'comment')

    """ #Disable the option to change the student or delivery terms
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].widget.attrs['disabled'] = True
        self.fields['terms_of_delivery'].widget.attrs['disabled'] = True """
