from django.shortcuts import render
from nutriplan.models import Alimentos

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
    
    proteinasObjetivo=int(CaloriasObjetivo*0.4/4)
    grasasObjetivo=int(CaloriasObjetivo*0.3/9)
    hidratosObjetivo=int(CaloriasObjetivo*0.3/4)
    
    global COMIDA_CHOICES
    COMIDA_CHOICES = (
        'Desayuno', 
        'Almuerzo', 
        'Merienda', 
        'Cena', 
    )
    
    # Envío el contexto
    context={
        'IMB':IMB,
        'CDM':CDM,
        'target':target,
        'CaloriasObjetivo':CaloriasObjetivo,
        'proteinasObjetivo':proteinasObjetivo,
        'grasasObjetivo':grasasObjetivo,
        'hidratosObjetivo':hidratosObjetivo,
        'alimentos': Alimentos.objects.all(),
        'COMIDA_CHOICES':COMIDA_CHOICES,
        }
    
    return render(request,'nutriplan/how-many-calories.html', context)

def dietPlan(request):
    # Obtengo los datos que vienen del formulario
    # Lo debo transformar en diccionario para poder contar los valores de cada key
    querydict=dict(request.POST)
    print(querydict)
    
    """ for comida in COMIDA_CHOICES:
        d=str(comida)+"1"
        print(d) """
        
    
    try:
        print(len(querydict['opcionesDesayuno']))
        for id in querydict['opcionesDesayuno']:
            print(id)
    except:
        pass
    try:
        print(len(querydict['opcionesAlmuerzo']))
    except:
        pass
    try:
        print(len(querydict['opcionesMerienda']))
    except:
        pass
    try:
        alimentosCena = list(querydict['opcionesCena'])
        alimentosCena=alimentosCena*7
        alimentosCena[0].append(789)
        
        print(alimentosCena)
        print(len(querydict['opcionesCena']))
        """
        la función solve() permite resolver sistemas de ecuaciones lineales de la forma Ax = b, donde A es una matriz de coeficientes, x es un vector de incógnitas y b es un vector de términos independientes.

        Por ejemplo, si quieres resolver el siguiente sistema de ecuaciones
        2x + 3y + z = 1
        x - 2y + 3z = -1
        3x + 2y - 4z = 0

        Puedes utilizar el siguiente código:

        import numpy as np

        # Definir la matriz de coeficientes A y el vector de términos independientes b
        A = np.array([[2, 3, 1], [1, -2, 3], [3, 2, -4]])
        b = np.array([1, -1, 0])

        # Resolver el sistema de ecuaciones utilizando la función solve() de numpy
        x = np.linalg.solve(A, b)

        # Imprimir la solución
        print(x)

        """
        import numpy as np

        # Definir la matriz de coeficientes A y el vector de términos independientes b
        A = np.array([[2, 3, 1], [1, -2, 3], [3, 2, -4]])
        b = np.array([1, -1, 0])

        # Resolver el sistema de ecuaciones utilizando la función solve() de numpy
        x = np.linalg.solve(A, b)

        # Imprimir la solución
        print(x)
    except:
        pass

    dias = range(1,8) #ok
    
    Dieta={
        'Desayuno':{
            'test':{'pan2':110, 'manteca2':130},
            'leche2':120,
            'manteca2':130,
            },
        'Almuerzo':{
            'test':{'pan':210, 'manteca':230},
            'leche':220,
            'manteca':230,
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
    #print(Desayuno[3])
    almuerzos=()
    meriendas=()
    cenas=()



    context={
        'COMIDA_CHOICES':COMIDA_CHOICES, #ok
        'dias': dias, #ok
        'Dieta': Dieta,
        }
        
    return render(request,'nutriplan/diet-plan.html', context) #ok


"""
Para resolver un sistema de 3 ecuaciones con 3 incógnitas en Python, puedes utilizar la biblioteca numpy. Esta biblioteca proporciona la función solve(), que permite resolver sistemas de ecuaciones lineales de la forma Ax = b, donde A es una matriz de coeficientes, x es un vector de incógnitas y b es un vector de términos independientes.

Por ejemplo, si quieres resolver el siguiente sistema de ecuaciones
2x + 3y + z = 1
x - 2y + 3z = -1
3x + 2y - 4z = 0

Puedes utilizar el siguiente código:

import numpy as np

# Definir la matriz de coeficientes A y el vector de términos independientes b
A = np.array([[2, 3, 1], [1, -2, 3], [3, 2, -4]])
b = np.array([1, -1, 0])

# Resolver el sistema de ecuaciones utilizando la función solve() de numpy
x = np.linalg.solve(A, b)

# Imprimir la solución
print(x)

"""