from django.urls import path
from .views import *

urlpatterns = [
    path('nutriplan', home, name="nutrihome"),
    path('nutriplan/cuantas_calorias_se_necesitan', cuantas_calorias_se_necesitan, name="cuantas_calorias_se_necesitan"),
    path('nutriplan/plan_de_dieta', plan_de_dieta, name="plan_de_dieta"),
]