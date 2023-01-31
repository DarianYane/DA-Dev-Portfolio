from django.urls import path
from .views import *

urlpatterns = [
    path("grade", grade_Home, name="grade-home"),
    path("grade/new-student", new_Student, name="new-student"),
    path("grade/new-rating", new_Rating, name="new-rating"),
]
