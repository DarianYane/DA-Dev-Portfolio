from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from grade.forms import StudentForm, RatingForm
from grade.models import Terms_of_Delivery, Tasks_to_Evaluate, Student


# Create your views here.
def grade_Home(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, "grade/00-home.html", context)


def new_Student(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(reverse("new_Rating_for_Student", args=[request.POST['name']]))

    context = {"form": form}

    return render(request, "grade/01-new-student.html", context)

def new_Rating(request):
    
    criterias = list(Tasks_to_Evaluate.objects.all())
    criterias = criterias[-3:]
    
    delivery_id=len(Terms_of_Delivery.objects.all())
    form = RatingForm(initial={'terms_of_delivery': delivery_id})
    
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("new-student")

    context = {
        "form": form,
        "criterias": criterias,
        }

    return render(request, "grade/09-new-rating.html", context)

def new_Rating_for_Student(request, name):
    
    criterias = list(Tasks_to_Evaluate.objects.all())
    criterias = criterias[-3:]
    
    name_id=len(Student.objects.all())
    delivery_id=len(Terms_of_Delivery.objects.all())
    form = RatingForm(initial={'student': name_id, 'terms_of_delivery': delivery_id})
    print(form)
    
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("new-student")

    context = {
        "form": form,
        "criterias": criterias,
        }

    return render(request, "grade/09-new-rating.html", context)

def test(request):
    post = request.POST
    print(post)
    return redirect("new-student")