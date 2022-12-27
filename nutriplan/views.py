from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse ("Hola Django - Coder")
    return render(request,'nutriplan/home.html')

def howManyCalories(request):
    print(request.POST)
    gender = request.POST.get('gender')
    weight = int(request.POST.get('weight'))
    height = int(request.POST.get('height'))
    age = int(request.POST.get('age'))
    print(gender)
    if gender == 'hombre':
        IMC = int( (10*weight) + (6.25*height) - (5*age) + 5)
    else:
        IMC = int( (10*weight) + (6.25*height) - (5*age) - 161)
    print(IMC)
    return HttpResponse ("Hola Django - Coder")
    #return render(request,'nutriplan/home.html')
