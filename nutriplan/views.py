from django.shortcuts import render
from nutriplan.models import Alimentos
import random

# Determino las constantes
COMIDA_CHOICES = (
    'Desayuno', 
    'Almuerzo', 
    'Merienda', 
    'Cena', 
)

dias = range(1,8)

# Create your views here.
def home(request):
    return render(request,'nutriplan/home.html')

def howManyCalories(request):
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
    
    return render(request,'nutriplan/how-many-calories.html', context)

def dietPlan(request):
    # Transformo en diccionario todas las instancias de mi db
    alimentos= Alimentos.objects.all()
    # Crear una lista vacía donde se almacenarán los alimentos
    listaAlimentos = []
    # Iterar sobre el queryset y crear un diccionario para cada persona
    for alimento in alimentos:
        datos_alimento = {
            'id': alimento.id,
            'nombre': alimento.nombre,
            'categoria': alimento.categoria,
            'comida': alimento.comida,
            'calorias': alimento.calorias,
            'hidratos': alimento.hidratos,
            'proteinas': alimento.proteinas,
            'grasas': alimento.grasas,
            'porcion': alimento.porcion,
        }
        listaAlimentos.append(datos_alimento)

    """ print(listaAlimentos) """
    
    # Obtengo los datos que vienen del formulario
    querydict=dict(request.POST)
    
    try:
        alimentosCenaFav = list(querydict['opcionesCena'])
        idFav1 = random.choice(alimentosCenaFav)
        alimento1=idFav1
        """ print(alimento1) """
    except:
        alimento1 = random.choice(listaAlimentos)['id']
        """ print(alimento1) """
    
    alimento2=random.choice(listaAlimentos)['id']
    """ print(alimento2) """
        
    alimento3=random.choice(listaAlimentos)['id']
    """ print(alimento3) """
    
    for alimento in listaAlimentos:
        if alimento['id']==alimento1:
            hidratos1=[]
            proteinas1=[]
            grasas1=[]
            hidratos1=(alimento['hidratos'])/100
            proteinas1=(alimento['proteinas'])/100
            grasas1=(alimento['grasas'])/100
            """ print(alimento1)
            print(hidratos1)
            print(proteinas1)
            print(grasas1) """
            print(grasas1)
            print(type(grasas1))
            
        if alimento['id']==alimento2:
            hidratos2=[]
            proteinas2=[]
            grasas2=[]
            hidratos2=(alimento['hidratos'])/100
            proteinas2=(alimento['proteinas'])/100
            grasas2=(alimento['grasas'])/100
            """ print(alimento2)
            print(hidratos2)
            print(proteinas2)
            print(grasas2) """
            
        if alimento['id']==alimento3:
            hidratos3=[]
            proteinas3=[]
            grasas3=[]
            hidratos3=(alimento['hidratos'])/100
            proteinas3=(alimento['proteinas'])/100
            grasas3=(alimento['grasas'])/100
            """ print(alimento3)
            print(hidratos3)
            print(proteinas3)
            print(grasas3) """


    
    """ la función solve() permite resolver sistemas de ecuaciones lineales de la forma Ax = b, donde A es una matriz de coeficientes, x es un vector de incógnitas y b es un vector de términos independientes.

        Por ejemplo, si quieres resolver el siguiente sistema de ecuaciones
        2x + 3y + z = 1
        x - 2y + 3z = -1
        3x + 2y - 4z = 0
        
        NOTAS:
            Los resultados son "b"
            las constantes (los array A) son los gramos de cada nutriente por cada gramo de ese alimento
            x, y y z van a ser los gramos de cada alimento (lo que quiero averiguar)

        Puedes utilizar el siguiente código: 

        import numpy as np

        # Definir la matriz de coeficientes A y el vector de términos independientes b
        A = np.array([[2, 3, 1], [1, -2, 3], [3, 2, -4]]) #([[hidratos de cada alimento/100],[proteinas de cada alimento/100],[grasas de cada alimento/100]])
        b = np.array([1, -1, 0])

        # Resolver el sistema de ecuaciones utilizando la función solve() de numpy
        x = np.linalg.solve(A, b)

        # Imprimir la solución
        print(x)"""
    
    import numpy as np
    
    hidratosDeCadaAlimento = [hidratos1, hidratos2, hidratos3]
    """ print(hidratos1)
    print(hidratos2)
    print(hidratos3)
    print(hidratosDeCadaAlimento) """
    proteinasDeCadaAlimento = [proteinas1, proteinas2, proteinas3]
    grasasDeCadaAlimento = [grasas1, grasas2, grasas3]
    
    # Definir la matriz de coeficientes A y el vector de términos independientes b
    nutrientesDeCadaAlimento = np.array([hidratosDeCadaAlimento, proteinasDeCadaAlimento, grasasDeCadaAlimento])
    print(nutrientesDeCadaAlimento)
    objetivos = np.array([hidratosObjetivo/4, proteinasObjetivo/4, grasasObjetivo/4])
    print(objetivos)

    # Resolver el sistema de ecuaciones utilizando la función solve() de numpy
    respuesta = np.linalg.solve(nutrientesDeCadaAlimento, objetivos)

    # Imprimir la solución
    print(respuesta)

    
    Dieta2={
        'Desayuno':{
            1:{
                'quesu':110,
                'leche':120,
                'manteca':130,
            },
            2:{
                'jamon':110,
                'tostada':120,
                'yogur':130,
            },
            3:{
                'quesu':110,
                'leche':120,
                'manteca':130,
            },
        },
    }
    
    """ uno = {}
    
    alimentosporcomida= Alimentos.objects.filter(comida="Desayuno")
    
    desayuno_aleatorio = random.choice(alimentosporcomida)
    print(desayuno_aleatorio)

    uno[desayuno_aleatorio.nombre] = desayuno_aleatorio.calorias
    
    desayuno_aleatorio = random.choice(alimentosporcomida)
    print(desayuno_aleatorio)

    uno[desayuno_aleatorio.nombre] = desayuno_aleatorio.calorias
    

    print(uno) """
    """ print(Dieta2['Desayuno'][1]) """
    
    
    """ print(Dieta2) """
    """ print(Dieta2['1']) """
    """ print(Dieta2) """



    #Esto es lo que tengo que ir generando automaticamente
    Dieta={
        'Desayuno':{
            1:{
                'quesu':110,
                'leche':120,
                'manteca':130,
            },
            2:{
                'jamon':110,
                'tostada':120,
                'yogur':130,
            },
            3:{
                'quesu':110,
                'leche':120,
                'manteca':130,
            },
            4:{
                'jamon':110,
                'tostada':120,
                'yogur':130,
            },
            5:{
                'jamon':110,
                'tostada':120,
                'yogur':130,
            },
            6:{
                'quesu':110,
                'leche':120,
                'manteca':130,
            },
            7:{
                'jamon':110,
                'tostada':120,
                'yogur':130,
            },
        },

        'Almuerzo':{
            1:{
                'arroz':110,
                'fideos':120,
                'carne':130,
            },
            2:{
                'empanadas':110,
                'ravioles':120,
                'pollo':130,
            },
        },
        
        'Merienda':{
            'test':{'pan':310, 'manteca':330},
            'leche':320,
            'manteca':330,
            },
        'Cena':{
            'test':{'pan':410, 'manteca':430},
            'leche':420,
            'manteca':430,
            },
        
        }
    
    """ print(Dieta) """
    

    
    """ for comida in COMIDA_CHOICES:
        d=str(comida)+"1"
        print(d) """
        
    




    context={
        'COMIDA_CHOICES':COMIDA_CHOICES, #ok
        'dias': dias, #ok
        'Dieta': Dieta, #ok
        }
        
    return render(request,'nutriplan/diet-plan.html', context) #ok

