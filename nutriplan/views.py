from django.shortcuts import render
from nutriplan.models import Alimentos
import random
import numpy as np

# Determino las constantes
COMIDA_CHOICES = (
    "Desayuno",
    "Almuerzo",
    "Merienda",
    "Cena",
)

dias = range(1, 8)

# Preparar la estructura para enviar en el context
Dieta = {}
for comida in COMIDA_CHOICES:
    Dieta[comida] = {}
    for n in dias:
        Dieta[comida][n] = {}

# Create your views here.
def nutrihome(request):
    return render(request, "nutriplan/nutrihome.html")


def cuantas_calorias_se_necesitan(request):
    # Obtengo los datos que vienen del formulario
    print(request.POST)
    gender = request.POST.get("gender")
    weight = int(request.POST.get("weight"))
    height = int(request.POST.get("height"))
    age = int(request.POST.get("age"))
    raf = request.POST.get("raf")
    objetivo = request.POST.get("objetivo")

    # Calculo el Índice Metabólico Basal (IMB)
    if gender == "hombre":
        IMB = int((10 * weight) + (6.25 * height) - (5 * age) + 5)
    else:
        IMB = int((10 * weight) + (6.25 * height) - (5 * age) - 161)
    print(f"IMB es {IMB}")

    # Convierto el Rango de Actividad Física (RAF) en valores numéricos
    if raf == "sedentario":
        IRAF = 1
    elif raf == "ligero":
        IRAF = 1.3
    elif raf == "moderado":
        IRAF = 1.5
    elif raf == "deportista":
        IRAF = 1.7
    print(f"IRAF es {IRAF}")

    # Calculo las Calorías de Mantenimiento (CDM)
    CDM = IMB * IRAF
    print(f"CDM es {CDM}")

    # Convierto el Objetivo en valores numéricos
    if objetivo == "adelgazar":
        ajuste = 0.85
        target = "perder peso"
    elif objetivo == "engordar":
        ajuste = 1.15
        target = "ganar masa muscular"
    print(f"ajuste es {ajuste}")

    # Calculo las calorías objetivo y los gramos correspondientes de cada nutriente
    CaloriasObjetivo = int(CDM * ajuste)
    print(f"CaloriasObjetivo es {CaloriasObjetivo}")

    # Nutrientes objetivos. Son globales para poder calcular la dieta
    global hidratosObjetivo
    hidratosObjetivo = int(CaloriasObjetivo * 0.3 / 4)
    print("hidratosObjetivo es", hidratosObjetivo)

    global proteinasObjetivo
    proteinasObjetivo = int(CaloriasObjetivo * 0.4 / 4)

    global grasasObjetivo
    grasasObjetivo = int(CaloriasObjetivo * 0.3 / 9)

    # Envío el contexto
    context = {
        "IMB": IMB,
        "CDM": CDM,
        "target": target,
        "CaloriasObjetivo": CaloriasObjetivo,
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
    }

    return render(request, "nutriplan/cuantas-calorias-se-necesitan.html", context)


def elegir_desayunos_favoritos(request):
    print(Dieta)

    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
    }

    return render(request, "nutriplan/elegir-desayunos-favoritos.html", context)


def verificar_positivo(respuesta):
    global grXalimento

    grXalimento = {}
    for i, gramos in enumerate(np.nditer(respuesta)):
        if gramos < 0:
            solved = 1 / 0
        if gramos > 20:
            key = nombreDeCadaAlimento[i]
            value = int(gramos)
            dictAliGr = {key: value}
            grXalimento.update(dictAliGr)


def solve(A, b):
    # Definir la matriz de coeficientes A y el vector de términos independientes b
    A = np.array(
        A
    )  # ([[hidratos de cada alimento/100],[proteinas de cada alimento/100],[grasas de cada alimento/100]])
    b = np.array(b)
    # Resolver el sistema de ecuaciones utilizando la función solve() de numpy
    respuesta = np.linalg.solve(A, b)

    # Imprimir la solución
    verificar_positivo(respuesta)


def calcular_desayunos(request):
    # print(request.POST)
    querydict = dict(request.POST)

    global proteinasDeCadaAlimento
    global hidratosDeCadaAlimento
    global grasasDeCadaAlimento
    global nombreDeCadaAlimento

    # Todos los Desayunos
    desayunosFiltrados = Alimentos.objects.filter(comida="Desayuno")
    # print('desayunosFiltrados es', desayunosFiltrados)

    for d in dias:
        solved = False
        while solved == False:
            hidratosDeCadaAlimento = []
            proteinasDeCadaAlimento = []
            grasasDeCadaAlimento = []
            nombreDeCadaAlimento = []

            # Verificar si hay Desayuno Fav
            idDesayunoFav = 0
            try:
                idDesayunoFav = int(random.choice(querydict["opcionesDesayuno"]))
            except:
                pass

            # SI hay desayuno Fav, se elige uno al azar como primer alimento del menú
            if idDesayunoFav != 0:
                print("hay deayuno Fav")
                DesayunoFav = Alimentos.objects.filter(id=idDesayunoFav)
                # print(DesayunoFav)

                # Iterar sobre el queryset y crear un diccionario para DesayunoFav
                for alimento in DesayunoFav:
                    datos_alimento = {
                        "id": alimento.id,
                        "nombre": alimento.nombre,
                        #'categoria': alimento.categoria,
                        #'comida': alimento.comida,
                        #'calorias': alimento.calorias,
                        "hidratos": alimento.hidratos,
                        "proteinas": alimento.proteinas,
                        "grasas": alimento.grasas,
                        #'porcion': alimento.porcion,
                    }

                    hidratosDeCadaAlimento.append(datos_alimento["hidratos"] / 100)
                    proteinasDeCadaAlimento.append(datos_alimento["proteinas"] / 100)
                    grasasDeCadaAlimento.append(datos_alimento["grasas"] / 100)
                    nombreDeCadaAlimento.append(datos_alimento["nombre"])
            else:
                # Si no hay desayuno Fav, se elige un alimento aleatoriamente como primer alimento del menú
                print("NOOOOO hay desayuno Fav")

                desayunoAleatorio = random.choice(desayunosFiltrados)

                hidratosDeCadaAlimento.append(desayunoAleatorio.hidratos / 100)
                proteinasDeCadaAlimento.append(desayunoAleatorio.proteinas / 100)
                grasasDeCadaAlimento.append(desayunoAleatorio.grasas / 100)
                nombreDeCadaAlimento.append(desayunoAleatorio.nombre)

            print(
                "hasta ahora:",
                hidratosDeCadaAlimento,
                proteinasDeCadaAlimento,
                grasasDeCadaAlimento,
                nombreDeCadaAlimento,
            )

            # Elegir otros 2 alimentos en forma aleatoria
            for r in range(2):
                desayunoAleatorio = random.choice(desayunosFiltrados)

                hidratosDeCadaAlimento.append(desayunoAleatorio.hidratos / 100)
                proteinasDeCadaAlimento.append(desayunoAleatorio.proteinas / 100)
                grasasDeCadaAlimento.append(desayunoAleatorio.grasas / 100)
                nombreDeCadaAlimento.append(desayunoAleatorio.nombre)

            print(hidratosDeCadaAlimento)
            print(proteinasDeCadaAlimento)
            print(grasasDeCadaAlimento)
            print(nombreDeCadaAlimento)

            # Intentar resolver las 3 ecuaciones con 3 incógnitas
            try:
                # Preparar A para solve
                A = [
                    hidratosDeCadaAlimento,
                    proteinasDeCadaAlimento,
                    grasasDeCadaAlimento,
                ]
                # Preparar b para solve
                b = [hidratosObjetivo / 4, proteinasObjetivo / 4, grasasObjetivo / 4]
                solve(A, b)

                # Si no arrojó error de matriz singular...
                solved = True

                # Actualizar la Dieta completa
                Dieta["Desayuno"][d] = grXalimento
            except:
                pass

    print(Dieta)

    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
    }

    return render(request, "nutriplan/elegir-almuerzos-favoritos.html", context)


def calcular_almuerzos(request):
    print(request.POST)
    querydict = dict(request.POST)
    
    global proteinasDeCadaAlimento
    global hidratosDeCadaAlimento
    global grasasDeCadaAlimento
    global nombreDeCadaAlimento
    
    # Todos los Almuerzos
    almuerzosFiltrados = Alimentos.objects.filter(comida="Almuerzo")
    print('almuerzosFiltrados es', almuerzosFiltrados)

    for d in dias:
        solved = False
        while solved == False:
            hidratosDeCadaAlimento = []
            proteinasDeCadaAlimento = []
            grasasDeCadaAlimento = []
            nombreDeCadaAlimento = []

            # Verificar si hay Almuerzo Fav
            idAlmuerzoFav = 0
            try:
                idAlmuerzoFav = int(random.choice(querydict["opcionesAlmuerzo"]))
            except:
                pass

            # SI hay almuerzo Fav, se elige uno al azar como primer alimento del menú
            if idAlmuerzoFav != 0:
                print("hay almuerzo Fav")
                AlmuerzoFav = Alimentos.objects.filter(id=idAlmuerzoFav)
                # print(AlmuerzoFav)

                # Iterar sobre el queryset y crear un diccionario para AlmuerzoFav
                for alimento in AlmuerzoFav:
                    datos_alimento = {
                        "id": alimento.id,
                        "nombre": alimento.nombre,
                        #'categoria': alimento.categoria,
                        #'comida': alimento.comida,
                        #'calorias': alimento.calorias,
                        "hidratos": alimento.hidratos,
                        "proteinas": alimento.proteinas,
                        "grasas": alimento.grasas,
                        #'porcion': alimento.porcion,
                    }

                    hidratosDeCadaAlimento.append(datos_alimento["hidratos"] / 100)
                    proteinasDeCadaAlimento.append(datos_alimento["proteinas"] / 100)
                    grasasDeCadaAlimento.append(datos_alimento["grasas"] / 100)
                    nombreDeCadaAlimento.append(datos_alimento["nombre"])
            else:
                # Si no hay almuerzo Fav, se elige un alimento aleatoriamente como primer alimento del menú
                print("NOOOOO hay almuerzo Fav")

                almuerzoAleatorio = random.choice(almuerzosFiltrados)

                hidratosDeCadaAlimento.append(almuerzoAleatorio.hidratos / 100)
                proteinasDeCadaAlimento.append(almuerzoAleatorio.proteinas / 100)
                grasasDeCadaAlimento.append(almuerzoAleatorio.grasas / 100)
                nombreDeCadaAlimento.append(almuerzoAleatorio.nombre)

            print(
                "hasta ahora:",
                hidratosDeCadaAlimento,
                proteinasDeCadaAlimento,
                grasasDeCadaAlimento,
                nombreDeCadaAlimento,
            )

            # Elegir otros 2 alimentos en forma aleatoria
            for r in range(2):
                almuerzoAleatorio = random.choice(almuerzosFiltrados)

                hidratosDeCadaAlimento.append(almuerzoAleatorio.hidratos / 100)
                proteinasDeCadaAlimento.append(almuerzoAleatorio.proteinas / 100)
                grasasDeCadaAlimento.append(almuerzoAleatorio.grasas / 100)
                nombreDeCadaAlimento.append(almuerzoAleatorio.nombre)

            print(hidratosDeCadaAlimento)
            print(proteinasDeCadaAlimento)
            print(grasasDeCadaAlimento)
            print(nombreDeCadaAlimento)

            # Intentar resolver las 3 ecuaciones con 3 incógnitas
            try:
                # Preparar A para solve
                A = [
                    hidratosDeCadaAlimento,
                    proteinasDeCadaAlimento,
                    grasasDeCadaAlimento,
                ]
                # Preparar b para solve
                b = [hidratosObjetivo / 4, proteinasObjetivo / 4, grasasObjetivo / 4]
                solve(A, b)

                # Si no arrojó error de matriz singular...
                solved = True

                # Actualizar la Dieta completa
                Dieta["Almuerzo"][d] = grXalimento
            except:
                pass
    
    print(Dieta)
    
    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
    }

    return render(request, "nutriplan/meriendas_favoritas.html", context)
