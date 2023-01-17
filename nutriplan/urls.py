from django.urls import path
from .views import *

urlpatterns = [
    path("nutriplan", nutrihome, name="nutrihome"),
    path(
        "nutriplan/cuantas-calorias-se-necesitan",
        cuantas_calorias_se_necesitan,
        name="cuantas_calorias_se_necesitan",
    ),
    path(
        "nutriplan/elegir-desayunos-favoritos",
        elegir_desayunos_favoritos,
        name="elegir_desayunos_favoritos",
    ),
    path(
        "nutriplan/elegir-almuerzos-favoritos",
        calcular_desayunos,
        name="elegir-almuerzos-favoritos",
    ),
    path(
        "nutriplan/meriendas_favoritas", calcular_almuerzos, name="meriendas_favoritas"
    ),
    # path('nutriplan/cenas_favoritas', cenas_favoritas, name="cenas_favoritas"),
    # path('nutriplan/plan_de_dieta', plan_de_dieta, name="plan_de_dieta"),
]
