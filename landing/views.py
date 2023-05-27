from django.shortcuts import render
from django.views.generic import ListView
from landing.models import Task

# For the contact form
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
# Task list for the roadmap
class Tasks_lists(ListView):
    queryset = Task.objects.all()
    context_object_name = "Tasks"

# Submission of contact form
def sendEmail(request):
    if request.method == "POST":
        template = render_to_string('landing/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
            })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['yanedarian.dev@gmail.com']
            )
        email.fail_silently = False
        email.send()
    return render(request,'landing/email_sent.html')

# SQl Cleaning Data Project
def sql_cleaning_data(request):
    return render(request,'landing/zz-sql-cleaning.html')

# Tableau Happiness Indicators Project
def happiness_indicators(request):
    return render(request,'landing/zz-happiness-indicators.html')

# Real API Project
def real_API_project(request):
    return render(request,'landing/zz-real_API_project.html')