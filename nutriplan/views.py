from django.shortcuts import render
from nutriplan.models import Alimentos
import random
import numpy as np

#Determine global variables
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

#Prepare the structure of the diet to be sent in context.
Dieta = {}
for comida in COMIDA_CHOICES:
    Dieta[comida] = {}
    for d in dias:
        Dieta[comida][d] = {}



# Create your views here.
#Homepage
def nutrihome(request):
    context = {
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    return render(request, "nutriplan/nutrihome.html", context)

#Determine how many calories are needed depending on the physiological characteristics of the person.
def cuantas_calorias_se_necesitan(request):
    #Obtain data coming from the form
    gender = request.POST.get("gender")
    weight = int(request.POST.get("weight"))
    height = int(request.POST.get("height"))
    age = int(request.POST.get("age"))
    raf = request.POST.get("raf")
    objetivo = request.POST.get("objetivo")

    #Calculation of Basal Metabolic Rate (BMR)
    if gender == "hombre":
        IMB = int((10 * weight) + (6.25 * height) - (5 * age) + 5)
    else:
        IMB = int((10 * weight) + (6.25 * height) - (5 * age) - 161)

    #Convert the Range of Physical Activity (RAF) to numerical values.
    if raf == "sedentario":
        IRAF = 1
    elif raf == "ligero":
        IRAF = 1.3
    elif raf == "moderado":
        IRAF = 1.5
    elif raf == "deportista":
        IRAF = 1.7
    
    #Calculating Calories of Maintenance (CDM)
    CDM = IMB * IRAF
    
    #Convert Target to numerical values
    if objetivo == "adelgazar":
        ajuste = 0.85
        target = "perder peso"
    elif objetivo == "engordar":
        ajuste = 1.15
        target = "ganar masa muscular"
    
    #Calculate target calories and corresponding grams of each nutrient
    CaloriasObjetivo = int(CDM * ajuste)
    
    #Target nutrients are calculated. These data are global in order to calculate the diet.
    global hidratosObjetivo
    hidratosObjetivo = int(CaloriasObjetivo * 0.3 / 4)
    
    global proteinasObjetivo
    proteinasObjetivo = int(CaloriasObjetivo * 0.4 / 4)
    
    global grasasObjetivo
    grasasObjetivo = int(CaloriasObjetivo * 0.3 / 9)
    
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

#Breakfasts are generated
def elegir_desayunos_favoritos(request):
    Dieta = {}
    for comida in COMIDA_CHOICES:
        Dieta[comida] = {}
        for d in dias:
            Dieta[comida][d] = {}
    #print(Dieta)
    context = {
        "hidratosObjetivo": hidratosObjetivo,
        "proteinasObjetivo": proteinasObjetivo,
        "grasasObjetivo": grasasObjetivo,
        "alimentos": Alimentos.objects.all(),
        "COMIDA_CHOICES": COMIDA_CHOICES,
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    return render(request, "nutriplan/elegir-desayunos-favoritos.html", context)

#Positive results are verified
def verificar_positivo(respuesta):
    global grXalimento
    grXalimento = {}
    for i, gramos in enumerate(np.nditer(respuesta)):
        #If the result is negative, generate an error to return to solve
        if gramos < 0:
            solved = 1 / 0
        #If it is more than 20 grams, the food deserves to be included in the menu.
        if gramos > 20:
            key = nombreDeCadaAlimento[i]
            value = int(gramos)
            dictAliGr = {key: value}
            grXalimento.update(dictAliGr)

#Solving the system of equations
def solve(A, b):
    #Define the coefficient matrix A and the vector of independent terms b
    A = np.array(A)
    b = np.array(b)
    #Solve the system of equations using numpy's solve() function
    respuesta = np.linalg.solve(A, b)
    #I send the answer as an argument to verify if all the heats are positive.
    verificar_positivo(respuesta)

#Generate the variables to determine the meals
def comida_y_alimentosFiltrados():
    global n_COMIDA_CHOICES
    n_COMIDA_CHOICES+=1
    
    global comida
    comida=COMIDA_CHOICES[n_COMIDA_CHOICES]
    
    global alimentosFiltrados
    alimentosFiltrados = Alimentos.objects.filter(comida=comida)

#The nutrients necessary for the system of equations that will solve the solve are sent to
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

#Loop that solves the system of equations for each meal.
def loop_diario():
    #Loop for each day
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
            
            #Check if there is a Favorite Food selected by user
            idAlimentoFav = 0
            global querydict
            
            try:
                idAlimentoFav = int(random.choice(querydict[f"opciones{comida}"]))
            except:
                pass
            
            #If they selected Fav Food, one is chosen at random as the first food on the menu.
            if idAlimentoFav != 0:
                AlimentoFav = Alimentos.objects.filter(id=idAlimentoFav)
                
                #Iterate on the queryset and create a dictionary for AlimentoFav
                for alimento in AlimentoFav:
                    datos_alimento = {
                        "id": alimento.id,
                        "nombre": alimento.nombre,
                        "hidratos": alimento.hidratos,
                        "proteinas": alimento.proteinas,
                        "grasas": alimento.grasas,
                    }
                    #Prepare lists for solve
                    hidratosDeCadaAlimento.append(datos_alimento["hidratos"] / 100)
                    proteinasDeCadaAlimento.append(datos_alimento["proteinas"] / 100)
                    grasasDeCadaAlimento.append(datos_alimento["grasas"] / 100)
                    nombreDeCadaAlimento.append(datos_alimento["nombre"])
            else:
                #If there is no Fav Food, a food is randomly chosen as the first food on the menu.
                listas_de_nutrientes_para_solve()
            
            
            #Choose 2 other foods at random
            for r in range(2):
                listas_de_nutrientes_para_solve()
            
            #Try to solve the 3 equations with 3 unknowns
            try:
                #Prepare A to solve
                A = [
                    hidratosDeCadaAlimento,
                    proteinasDeCadaAlimento,
                    grasasDeCadaAlimento,
                ]
                #Prepare b to solve
                b = [
                    hidratosObjetivo / 4,
                    proteinasObjetivo / 4,
                    grasasObjetivo / 4
                ]
                
                solve(A, b)
                
                #If there was no singular matrix error and all the answers are positive values, exit while
                solved = True
                
                #Update Diet
                Dieta[f"{comida}"][d] = grXalimento
            except:
                pass

#Calculate breakfasts
def calcular_desayunos(request):
    global querydict
    querydict = dict(request.POST)
    
    global n_COMIDA_CHOICES
    #Start an iteration per COMIDA_CHOICES in order to loop the process for each meal of the day.
    n_COMIDA_CHOICES=-1
    
    comida_y_alimentosFiltrados()
    loop_diario()
    #print(Dieta)
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

#Calculate lunches
def calcular_almuerzos(request):
    global querydict
    querydict = dict(request.POST)
    
    comida_y_alimentosFiltrados()
    loop_diario()
    #print(Dieta)
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

#Calculate snacks
def calcular_meriendas(request):
    global querydict
    querydict = dict(request.POST)
    
    comida_y_alimentosFiltrados()
    loop_diario()
    #print(Dieta)
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

#Calculate dinners
def calcular_cenas(request):
    global querydict
    querydict = dict(request.POST)
    
    comida_y_alimentosFiltrados()
    loop_diario()
    #print(Dieta)
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

#Filter foods according to the category to which they belong.
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

#Return a rendering for the English FAQ
def FAQENG(request):
    context = {
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    return render(request, 'nutriplan/FAQ-ENG.html', context)

#Return a rendering for the Spanish FAQ
def FAQES(request):
    context = {
        "CATEGORIA_CHOICES": CATEGORIA_CHOICES,
    }
    return render(request, 'nutriplan/FAQ-ES.html', context)