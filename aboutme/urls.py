from django.urls import path
from aboutme.views import aboutmehome


urlpatterns = [
    path('aboutme', aboutmehome, name="about me home"),
]