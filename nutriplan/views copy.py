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

#Preparar la estructura para enviar en el context
Menu={}
for comida in COMIDA_CHOICES:
    Menu[comida]={}
    for n in dias:
        Menu[comida][n]={}


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
    # Obtener los datos que vienen del formulario
    querydict=dict(request.POST)
    for n in dias:
        # Iterar un menú para las 4 comidas
        for comida in COMIDA_CHOICES:        
            # Transformar en diccionario todas las instancias de mi db
            alimentos= Alimentos.objects.filter(comida=comida)
            
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
            
            # Crear una lista vacía donde se almacenarán los alimentos seleccionados
            alimentosSeleccionados=[]
            
            # Intentar obtener las opciones favoritas del usuario, y a partir del id, obtener la instancia
            try:
                idalimentosCenaFav = list(querydict['opciones%' % comida])
                idFav1 = int(random.choice(idalimentosCenaFav))
                for alimento in listaAlimentos:
                    if alimento['id']==idFav1:
                        alimento1=alimento
            except:
                alimento1 = random.choice(listaAlimentos)
        
            # Eliminar el elemento seleccionado de la lista de alimentos para que no se incluya 2 veces en una comida
            listaAlimentos.remove(alimento1)
            
            # Construir la lista de los 3 alimentos que tendrá cada comida
            alimentosSeleccionados.append(alimento1)
            
            # Variable que cambia de estado cuando se encuentra una solcuion satisfactoria al sistema de ecuaciones
            solved = False
            
            for i in range(2):
                        alimentoAleatorio=random.choice(listaAlimentos)
                        alimentosSeleccionados.append(alimentoAleatorio)
                        # Eliminar el elemento seleccionado de la lista de alimentos para que no se incluya 2 veces en una comida
                        listaAlimentos.remove(alimentoAleatorio)
                        
                        

            import numpy as np
            # Iterar mientras no se encuentre una solucion satisfactoria
            while solved==False:
                #print(solved)
                try:
                    # Agregar 2 alimentos aleatorios
                    for i in range(3):
                        alimentoAleatorio=random.choice(listaAlimentos)
                        alimentosSeleccionados.append(alimentoAleatorio)
                        # Eliminar el elemento seleccionado de la lista de alimentos para que no se incluya 2 veces en una comida
                        listaAlimentos.remove(alimentoAleatorio)

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
                    
                    
                    print(alimentosSeleccionados)
                    
                    # Preparar los array coeficientes
                    hidratosDeCadaAlimento=[]
                    proteinasDeCadaAlimento=[]
                    grasasDeCadaAlimento=[]
                    
                    for alimentosSeleccionado in alimentosSeleccionados:
                        # Hidratos
                        hidratos=(alimentosSeleccionado.get('hidratos'))/100
                        hidratosDeCadaAlimento.append(hidratos)
                        # Proteinas
                        proteinas=(alimentosSeleccionado.get('proteinas'))/100
                        proteinasDeCadaAlimento.append(proteinas)
                        # Grasas
                        grasas=(alimentosSeleccionado.get('grasas'))/100
                        grasasDeCadaAlimento.append(grasas)
                    
                    # Definir la matriz de coeficientes A
                    nutrientesDeCadaAlimento = np.array([
                        hidratosDeCadaAlimento, 
                        proteinasDeCadaAlimento, 
                        grasasDeCadaAlimento
                        ])
                    # Definir l vector de resultaods b
                    objetivos = np.array([
                        hidratosObjetivo/4, 
                        proteinasObjetivo/4, 
                        grasasObjetivo/4
                        ])
                    # Resolver el sistema de ecuaciones utilizando la función solve() de numpy
                    respuesta = np.linalg.solve(nutrientesDeCadaAlimento, objetivos)
                    # Imprimir la solución
                    #print(respuesta)
                    
                    
                    # Verificar que los componentes de la respuesta sean positivos
                    # y armar los diccionarios {nombre:gramos} para cada alimento
                    x=0
                    grXalimento=[]
                    for resp in np.nditer(respuesta):
                        value = float(resp)
                        # Si hay un valor negativo, levantar un error para que el while vuelva a empezar
                        if value<0:
                            solved=1/0
                        
                        key=alimentosSeleccionados[x].get('nombre')
                        dictAliGr={key:value}
                        x+=1
                        grXalimento.append(dictAliGr) # TODO grXalimento es lo que debe ir dentro de la matriz dieta

                    # Si no generó un error la matriz y no hay valores negativos, frenar la iteración
                    solved=True
                    
                    # Agregar la combinacion de alimentos y gramos al diccionario general
                    #diccionario1["otro_diccionario"] = diccionario2
                    Menu[comida][n]=grXalimento
                
                except:
                    for i in range(2):
                        # Devolver a la lista de alimentos los 2 alientos elegidos en forma aleatoria
                        listaAlimentos.append(alimentosSeleccionados[len(alimentosSeleccionados)-1])
                        # Eliminar de los alimentos seleccionados los 2 alientos elegidos en forma aleatoria (solo queda 1 de los favoritos)
                        alimentosSeleccionados.pop()
    
    
    print(Menu)







    """ for alimentosSeleccionado in alimentosSeleccionados:
        print(alimentosSeleccionado.get('nombre')) """
    
    
    
    
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




    context={
        'COMIDA_CHOICES':COMIDA_CHOICES, #ok
        'dias': dias, #ok
        'Dieta': Dieta, #ok
        }
        
    return render(request,'nutriplan/diet-plan.html', context) #ok
