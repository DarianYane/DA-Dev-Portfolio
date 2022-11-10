from django.shortcuts import render
from django.views.generic import ListView
from landing.models import Task

# For the contact form
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse


# Create your views here.
"""
def home(request):
    return render(request,"landing/index.html")
    """


class Tasks_lists(ListView):
    queryset = Task.objects.all()
    context_object_name = "Tasks"

# For the contact form
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