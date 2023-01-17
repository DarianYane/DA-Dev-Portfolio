from django.shortcuts import render
from nutriplan.models import Alimentos
import random
import numpy as np

# Determino las constantes
COMIDA_CHOICES = (
    'Desayuno', 
    'Almuerzo', 
    'Merienda', 
    'Cena', 
)

dias = range(1,2)

#Preparar la estructura para enviar en el context
Dieta={}
for comida in COMIDA_CHOICES:
    Dieta[comida]={}
    for n in dias:
        Dieta[comida][n]={}

# Create your views here.
def home(request):
    return render(request,'nutriplan/home.html')

def cuantas_calorias_se_necesitan(request):
    # Obtengo los datos que vienen del formulario
    print(request.POST)
    gender = request.POST.get('gender')
    weight = int(request.POST.get('weight'))
    height = int(request.POST.get('height'))
    age = int(request.POST.get('age'))
    raf = request.POST.get('raf')
    objetivo = request.POST.get('objetivo')
    
    # Calculo el Índice Metabólico Basal (IMB)
    if gender == 'hombre':
        IMB = int( (10*weight) + (6.25*height) - (5*age) + 5)
    else:
        IMB = int( (10*weight) + (6.25*height) - (5*age) - 161)
    print(f'IMB es {IMB}')
    
    # Convierto el Rango de Actividad Física (RAF) en valores numéricos
    if raf == 'sedentario':
        IRAF = 1
    elif raf == 'ligero':
        IRAF = 1.3
    elif raf == 'moderado':
        IRAF = 1.5
    elif raf == 'deportista':
        IRAF = 1.7
    print(f'IRAF es {IRAF}')
    
    # Calculo las Calorías de Mantenimiento (CDM)
    CDM = IMB*IRAF
    print(f'CDM es {CDM}')
    
    # Convierto el Objetivo en valores numéricos
    if objetivo == 'adelgazar':
        ajuste = 0.85
        target = 'perder peso'
    elif objetivo == 'engordar':
        ajuste = 1.15
        target = 'ganar masa muscular'
    print(f'ajuste es {ajuste}')
    
    # Calculo las calorías objetivo y los gramos correspondientes de cada nutriente
    CaloriasObjetivo = int(CDM*ajuste)
    print(f'CaloriasObjetivo es {CaloriasObjetivo}')
    
    # Nutrientes objetivos. Son globales para poder calcular la dieta
    global hidratosObjetivo
    hidratosObjetivo=int(CaloriasObjetivo*0.3/4)
    
    global proteinasObjetivo
    proteinasObjetivo=int(CaloriasObjetivo*0.4/4)
    
    global grasasObjetivo
    grasasObjetivo=int(CaloriasObjetivo*0.3/9)

    
    # Envío el contexto
    context={
        'IMB':IMB,
        'CDM':CDM,
        'target':target,
        'CaloriasObjetivo':CaloriasObjetivo,
        'hidratosObjetivo':hidratosObjetivo,
        'proteinasObjetivo':proteinasObjetivo,
        'grasasObjetivo':grasasObjetivo,
        'alimentos': Alimentos.objects.all(),
        'COMIDA_CHOICES':COMIDA_CHOICES,
        }
    
    return render(request,'nutriplan/cuantas_calorias_se_necesitan.html', context)

def verificar_positivo(respuesta):
    global grXalimento
    
    grXalimento={}
    for i,gramos in enumerate(np.nditer(respuesta)):
        if gramos<0:
            solved=1/0
        if gramos>20:
            key=nombreDeCadaAlimento[i]
            value=int(gramos)
            dictAliGr={key:value}
            grXalimento.update(dictAliGr)

def solve(A,b):
    # Definir la matriz de coeficientes A y el vector de términos independientes b
    A = np.array(A) #([[hidratos de cada alimento/100],[proteinas de cada alimento/100],[grasas de cada alimento/100]])
    b = np.array(b)
    # Resolver el sistema de ecuaciones utilizando la función solve() de numpy
    respuesta = np.linalg.solve(A, b)
    
    # Imprimir la solución
    verificar_positivo(respuesta)

def DA(alimento):
    print(alimento)
    print(type(alimento))
    datos_alimento = {
        #'id': alimento.id,
        'nombre': alimento.nombre,
        #'categoria': alimento.categoria,
        #'comida': alimento.comida,
        #'calorias': alimento.calorias,
        'hidratos': alimento.hidratos,
        'proteinas': alimento.proteinas,
        'grasas': alimento.grasas,
        #'porcion': alimento.porcion,
    }
    
    hidratos=(datos_alimento.get('hidratos'))/100
    hidratosDeCadaAlimento.append(hidratos)
    # Proteinas
    proteinas=(datos_alimento.get('proteinas'))/100
    proteinasDeCadaAlimento.append(proteinas)
    # Grasas
    grasas=(datos_alimento.get('grasas'))/100
    grasasDeCadaAlimento.append(grasas)
    # Nombres
    nombre=(datos_alimento.get('nombre'))
    nombreDeCadaAlimento.append(nombre)


def alimento1(alimentosFiltrados, querydict):
    global proteinasDeCadaAlimento
    global hidratosDeCadaAlimento
    global grasasDeCadaAlimento
    global nombreDeCadaAlimento
    
    hidratosDeCadaAlimento=[]
    proteinasDeCadaAlimento=[]
    grasasDeCadaAlimento=[]
    nombreDeCadaAlimento=[]
    
    try:        
        idAlimentoFav = int(random.choice(querydict[f'opciones{comida}']))
        
        print('idAlimentoFav es un ',type(idAlimentoFav))
        
        #alimento1 = Alimentos.objects.filter(id=idAlimentoFav)
        

        for alimento in alimentosFiltrados:
            if alimento.id == idAlimentoFav:
                print('print(idAlimentoFav) es ',idAlimentoFav)
                print('alimento.id es ', alimento.id)
                print('iffffffff esss ',alimento)
                print('alimento es ',type(alimento))
                DA(alimento)
        """ alimento=random.choice(alimentosFiltrados)
        DA(alimento) """
    except:
        alimento=random.choice(alimentosFiltrados)
        DA(alimento)

def alimentos2y3(alimentosFiltrados):
    
    for r in range(2):
        alimento=random.choice(alimentosFiltrados)
        DA(alimento)

def plan_de_dieta(request):
    # Obtener los datos que vienen del formulario
    querydict=dict(request.POST)
    print('querydict es ',querydict) #***********
    
    for comida in COMIDA_CHOICES:
        alimentosFiltrados= Alimentos.objects.filter(comida=comida)

        for d in dias:
            
            solved=False
            while solved==False:
                try:
                    #elegir_alimentos_y_HPG(alimentosFiltrados,querydict)
                    alimento1(alimentosFiltrados, querydict)
                    alimentos2y3(alimentosFiltrados)
                    # Preparar A para solve
                    A=[
                        hidratosDeCadaAlimento, 
                        proteinasDeCadaAlimento, 
                        grasasDeCadaAlimento
                    ]
                    # Preparar b para solve
                    b=[
                        hidratosObjetivo/4, 
                        proteinasObjetivo/4, 
                        grasasObjetivo/4
                    ]
                    solve(A,b)
                    
                    # Si no arrojó error de matriz singular...
                    solved=True

                    Dieta[comida][d]=grXalimento
                except:
                    pass
    
    
    #print(Dieta)
    #print(variable15)

    context={
        'COMIDA_CHOICES':COMIDA_CHOICES, #ok
        'dias': dias, #ok
        'Dieta': Dieta, #ok
        }
        
    return render(request,'nutriplan/plan_de_dieta.html', context) #ok
