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

CATEGORIA_CHOICES = (
    'Frutas',
    'Verduras',
    'Grasas',
    'Cereales_Legumbres',
    'Proteínas',
    'Lacteos',
    'Otros',
)

dias = range(1, 8)

# Preparar la estructura para enviar en el context
Dieta = {}
for comida in COMIDA_CHOICES:
    Dieta[comida] = {}
    for d in dias:
        Dieta[comida][d] = {}



# Create your views here.

def nutrihome(request):
    context = {
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    return render(request, "nutriplan/nutrihome.html", context)


def cuantas_calorias_se_necesitan(request):
    # Obtengo los datos que vienen del formulario
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

    # Convierto el Rango de Actividad Física (RAF) en valores numéricos
    if raf == "sedentario":
        IRAF = 1
    elif raf == "ligero":
        IRAF = 1.3
    elif raf == "moderado":
        IRAF = 1.5
    elif raf == "deportista":
        IRAF = 1.7
    
    # Calculo las Calorías de Mantenimiento (CDM)
    CDM = IMB * IRAF
    
    # Convierto el Objetivo en valores numéricos
    if objetivo == "adelgazar":
        ajuste = 0.85
        target = "perder peso"
    elif objetivo == "engordar":
        ajuste = 1.15
        target = "ganar masa muscular"
    
    # Calculo las calorías objetivo y los gramos correspondientes de cada nutriente
    CaloriasObjetivo = int(CDM * ajuste)
    
    # Nutrientes objetivos. Son globales para poder calcular la dieta
    global hidratosObjetivo
    hidratosObjetivo = int(CaloriasObjetivo * 0.3 / 4)
    
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
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    
    return render(request, "nutriplan/cuantas-calorias-se-necesitan.html", context)


def elegir_desayunos_favoritos(request):
    Dieta = {}
    for comida in COMIDA_CHOICES:
        Dieta[comida] = {}
        for d in dias:
            Dieta[comida][d] = {}
    
    print(Dieta)
    
    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    
    return render(request, "nutriplan/elegir-desayunos-favoritos.html", context)


def verificar_positivo(respuesta):
    global grXalimento

    grXalimento = {}
    for i, gramos in enumerate(np.nditer(respuesta)):
        # Si el resultado es negativo, generar un error para volver al solve
        if gramos < 0:
            solved = 1 / 0
        # Si son más de 20 gramos, el alimento merece ser incluído en el menú
        if gramos > 20:
            key = nombreDeCadaAlimento[i]
            value = int(gramos)
            dictAliGr = {key: value}
            grXalimento.update(dictAliGr)


def solve(A, b):
    # Definir la matriz de coeficientes A y el vector de términos independientes b
    A = np.array(A)
    
    b = np.array(b)
    
    # Resolver el sistema de ecuaciones utilizando la función solve() de numpy
    respuesta = np.linalg.solve(A, b)
    
    # Verificar si todas las respuestas son valores positivos
    verificar_positivo(respuesta)


def comida_y_alimentosFiltrados():
    # Comenzar el menú para la primera comida
    global n_COMIDA_CHOICES
    n_COMIDA_CHOICES+=1
    
    global comida
    comida=COMIDA_CHOICES[n_COMIDA_CHOICES]
    
    # Traer todos los alimentos de esa comida
    global alimentosFiltrados
    alimentosFiltrados = Alimentos.objects.filter(comida=comida)


def listas_de_nutrientes_para_solve():
    alimentoAleatorio = random.choice(alimentosFiltrados)
    
    global hidratosDeCadaAlimento
    global proteinasDeCadaAlimento
    global grasasDeCadaAlimento
    global nombreDeCadaAlimento
    
    hidratosDeCadaAlimento.append(alimentoAleatorio.hidratos / 100)
    proteinasDeCadaAlimento.append(alimentoAleatorio.proteinas / 100)
    grasasDeCadaAlimento.append(alimentoAleatorio.grasas / 100)
    nombreDeCadaAlimento.append(alimentoAleatorio.nombre)


def loop_diario():
    # Hacer el loop para cada día
    for d in dias:
        solved = False
        while solved == False:
            global hidratosDeCadaAlimento
            global proteinasDeCadaAlimento
            global grasasDeCadaAlimento
            global nombreDeCadaAlimento
            
            hidratosDeCadaAlimento = []
            proteinasDeCadaAlimento = []
            grasasDeCadaAlimento = []
            nombreDeCadaAlimento = []
            
            # Verificar si hay Alimento Fav
            idAlimentoFav = 0
            global querydict
            
            try:
                idAlimentoFav = int(random.choice(querydict[f"opciones{comida}"]))
            except:
                pass
            
            # Si seleccionaron Alimento Fav, se elige uno al azar como primer alimento del menú
            if idAlimentoFav != 0:
                AlimentoFav = Alimentos.objects.filter(id=idAlimentoFav)
                
                # Iterar sobre el queryset y crear un diccionario para AlimentoFav
                for alimento in AlimentoFav:
                    datos_alimento = {
                        "id": alimento.id,
                        "nombre": alimento.nombre,
                        "hidratos": alimento.hidratos,
                        "proteinas": alimento.proteinas,
                        "grasas": alimento.grasas,
                    }
                    # Preparar las listas para el solve
                    hidratosDeCadaAlimento.append(datos_alimento["hidratos"] / 100)
                    proteinasDeCadaAlimento.append(datos_alimento["proteinas"] / 100)
                    grasasDeCadaAlimento.append(datos_alimento["grasas"] / 100)
                    nombreDeCadaAlimento.append(datos_alimento["nombre"])
            else:
                # Si no hay Alimento Fav, se elige un alimento aleatoriamente como primer alimento del menú
                listas_de_nutrientes_para_solve()
            
            
            # Elegir otros 2 alimentos en forma aleatoria
            for r in range(2):
                listas_de_nutrientes_para_solve()
            
            # Intentar resolver las 3 ecuaciones con 3 incógnitas
            try:
                # Preparar A para solve
                A = [
                    hidratosDeCadaAlimento,
                    proteinasDeCadaAlimento,
                    grasasDeCadaAlimento,
                ]
                # Preparar b para solve
                b = [
                    hidratosObjetivo / 4,
                    proteinasObjetivo / 4,
                    grasasObjetivo / 4
                ]
                
                solve(A, b)
                
                # Si no arrojó error de matriz singular y todas las respuestas son valores positivas, salir del while
                solved = True
                
                # Actualizar la Dieta completa
                Dieta[f"{comida}"][d] = grXalimento
            except:
                pass


def calcular_desayunos(request):
    global querydict
    querydict = dict(request.POST)
    
    global n_COMIDA_CHOICES
    # Inicio una iteración por COMIDA_CHOICES para poder loopear el proceso para cada comida del día
    n_COMIDA_CHOICES=-1
    
    comida_y_alimentosFiltrados()
    
    loop_diario()
    
    print(Dieta)
    
    global context
    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
        "n_COMIDA_CHOICES": n_COMIDA_CHOICES,
    }
    
    return render(request, "nutriplan/elegir-almuerzos-favoritos.html", context)

def calcular_almuerzos(request):
    global querydict
    querydict = dict(request.POST)
    
    comida_y_alimentosFiltrados()
    
    loop_diario()
    
    print(Dieta)
    
    global context
    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
        "n_COMIDA_CHOICES": n_COMIDA_CHOICES,
    }
    
    return render(request, "nutriplan/elegir-meriendas-favoritas.html", context)

def calcular_meriendas(request):
    global querydict
    querydict = dict(request.POST)
    
    comida_y_alimentosFiltrados()
    
    loop_diario()
    
    print(Dieta)
    
    global context
    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
        "n_COMIDA_CHOICES": n_COMIDA_CHOICES,
    }
    
    return render(request, "nutriplan/elegir-cenas-favoritas.html", context)

def calcular_cenas(request):
    global querydict
    querydict = dict(request.POST)
    
    comida_y_alimentosFiltrados()
    
    loop_diario()
    
    print(Dieta)
    
    global context
    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
        "dias": dias,
        "Dieta": Dieta,
    }
    
    return render(request, "nutriplan/dieta-plan.html", context)

def alimentos_por_categoria(request, categoria):
    Categoria_de_alimentos = categoria
    if categoria == "Proteínas":
        Categoria_de_alimentos = "Proteinas"
    elif Categoria_de_alimentos == "Cereales_Legumbres":
            Categoria_de_alimentos = "Cereales y Legumbres"
    else:
        Categoria_de_alimentos = categoria
    
    
    queryset = Alimentos.objects.filter(categoria=Categoria_de_alimentos)
    
    alimentos_por_categoria = []
    
    for alimento in queryset:
        datos_alimento = {
            "id": alimento.id,
            "nombre": alimento.nombre,
            "hidratos": alimento.hidratos,
            "proteinas": alimento.proteinas,
            "grasas": alimento.grasas,
            "calorias": alimento.calorias,
            "comida": alimento.comida,
            "porcion": alimento.porcion,
        }
        alimentos_por_categoria.append(datos_alimento)
    
    
    context={
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
        "alimentos_por_categoria": alimentos_por_categoria,
        "Categoria_de_alimentos": Categoria_de_alimentos,
    }
    
    return render(request, 'nutriplan/alimentos-por-categoria.html', context)

def FAQENG(request):
    context = {
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    return render(request, 'nutriplan/FAQ-ENG.html', context)

def FAQES(request):
    context = {
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    return render(request, 'nutriplan/FAQ-ES.html', context)