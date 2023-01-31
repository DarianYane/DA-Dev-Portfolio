from django.shortcuts import render, redirect
from grade.forms import StudentForm, RatingForm
from grade.models import Terms_of_Delivery, Tasks_to_Evaluate


# Create your views here.
def grade_Home(request):
    context = {}
    return render(request, "grade/00-home.html", context)


def new_Student(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("new-rating")

    context = {"form": form}

    return render(request, "grade/01-new-student.html", context)

    """ context={
        
    }
    return render(request,'grade/01-new-student.html', context) """


def new_Rating(request):
    
    tasks = Tasks_to_Evaluate.objects.all()
    for i in tasks:
        print(i)
    
    form = RatingForm()
    
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("new-student")

    context = {
        "form": form,
        "tasks": tasks,
        }

    return render(request, "grade/09-new-rating.html", context)
