from django.urls import path
from .views import *

urlpatterns = [
    path(
        "nutriplan",
        nutrihome,
        name="nutrihome"
    ),
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
        "nutriplan/elegir-meriendas-favoritas",
        calcular_almuerzos,
        name="elegir-meriendas-favoritas"
    ),
    path(
        "nutriplan/elegir-cenas-favoritas",
        calcular_meriendas,
        name="elegir-cenas-favoritas"
    ),
    path(
        "nutriplan/dieta-plan",
        calcular_cenas,
        name="dieta-plan"
    ),
]
