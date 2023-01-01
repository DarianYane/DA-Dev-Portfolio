from django.urls import path
from .views import *

urlpatterns = [
    path('nutriplan', home, name="nutrihome"),
    path('nutriplan/how-many-calories', howManyCalories, name="howManyCalories"),
]