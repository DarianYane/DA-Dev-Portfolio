from django.shortcuts import render

# Create your views here.
def aboutmehome(request):
    return render(request, 'aboutme/home.html')