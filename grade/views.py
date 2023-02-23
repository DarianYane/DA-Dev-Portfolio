from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView
from .forms import UpdateRatingForm #UpdatePostForm
from grade.forms import StudentForm, RatingForm
from grade.models import Terms_of_Delivery, Tasks_to_Evaluate, Student, Rating

# Create your views here.
#Student roster
def grade_Home(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, "grade/00-home.html", context)

#Create a student
def new_Student(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(reverse("new_Rating_for_Student", args=[request.POST['name']]))

    context = {"form": form}

    return render(request, "grade/01-new-student.html", context)

#Create a generic rating
def new_Rating(request):
    post=request.POST.get('buttonto')
    #List the criteria for delivery
    criterias = list(Tasks_to_Evaluate.objects.all())
    criterias = criterias[-3:]
    
    delivery_id=len(Terms_of_Delivery.objects.all())
    form = RatingForm(initial={'terms_of_delivery': delivery_id})
    #Depending on the button pressed when submitting the form, it redirects to a different page.
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            if post == 'Submit and Create a New Student':
                print('to New Student')
                return redirect("new-student")
            if post == 'Submit and Create a New Rating':
                print('to New Rating')
                return redirect("new-rating")
            if post == 'Submit and Back to Home':
                print('to Home')
                return redirect("grade-home")

    context = {
        "form": form,
        "criterias": criterias,
        }
    return render(request, "grade/09-new-rating.html", context)

#Create a rating after creating a student
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

#Search by student
def student_Search(request):    
    if request.GET['student_search']:
        queryset = request.GET['student_search']
        #Filter by selected name
        selected_student = Student.objects.filter(name=queryset)
        for i in selected_student:
            #Get the id of the selected name
            ratings = Rating.objects.filter(student_id=i.id)
            if ratings!=[]:
                return render(request, 'grade/20-student_search_result.html', {'ratings': ratings, 'wanted_student': queryset})
    else:
        #If a valid search is not performed
        queryset = '(No search performed)'
        print(queryset)
        return render(request, 'grade/20-student_search_result.html', {'search': queryset})
    return redirect('grade-home')
 
#Update a rating
class UpdateRatingView(UpdateView):
    model = Rating
    form_class = UpdateRatingForm
    template_name = "grade/25-edit-rating.html"