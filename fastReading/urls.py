"""FastReading URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from fastReading.views import upload, wipuf, f2_bolded, DownloadPDF

#In order to upload a file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bolded', f2_bolded, name='f2_bolded'),
    path('', upload, name='upload'),
    path('pdf_download/', DownloadPDF.as_view(), name="pdf_download"),
    path('fastReading/wipuf', wipuf, name="fastReading/wipuf"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)