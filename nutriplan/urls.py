from django.urls import path
from .views import *

urlpatterns = [
    path('nutriplan', home, name="home"),
    path('nutriplan/how-many-calories', howManyCalories, name="howManyCalories"),
]