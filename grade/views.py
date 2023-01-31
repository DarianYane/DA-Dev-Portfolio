from django.shortcuts import render
from grade.models import *

# Create your views here.
def rating(request):
    return render(request,'grade/rating.html')