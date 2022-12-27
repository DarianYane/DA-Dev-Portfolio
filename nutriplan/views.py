from django.shortcuts import render
from django.http import HttpResponse

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
    #print(gender)
    
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
    
    proteinas=int(CaloriasObjetivo*0.4/4)
    grasas=int(CaloriasObjetivo*0.3/9)
    hidratos=int(CaloriasObjetivo*0.3/4)
    
    # Envío el contexto
    context={
        'IMB':IMB,
        'CDM':CDM,
        'target':target,
        'CaloriasObjetivo':CaloriasObjetivo,
        'proteinas':proteinas,
        'grasas':grasas,
        'hidratos':hidratos,
        }
    
    return render(request,'nutriplan/how-many-calories.html', context)
