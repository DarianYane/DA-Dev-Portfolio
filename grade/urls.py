from django.urls import path
from .views import *

urlpatterns = [
    path("grade", grade_Home, name="grade-home"),
    path("grade/new-student", new_Student, name="new-student"),
    path("grade/new-rating", new_Rating, name="new-rating"),
    path("grade/new-rating/<str:name>/", new_Rating_for_Student, name="new_Rating_for_Student"),
    path("grade/student-search/", student_Search, name="student-search"),
    path('grade/update-grade/<int:pk>', UpdateRatingView.as_view(), name="UpdateRatingView"),
]
