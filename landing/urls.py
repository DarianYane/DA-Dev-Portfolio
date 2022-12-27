from django.urls import path
from fastReading.views import upload
from aboutme.views import aboutmehome
from blog.views import BlogListView
from landing import views
from nutriplan.views import home

urlpatterns = [
    path('fastReading/upload', upload, name="fastReading/upload"),
    path('aboutme', aboutmehome, name="about me home"),
    path('', views.Tasks_lists.as_view(), name="home"),
    path('blog', BlogListView.as_view(), name="BlogListView"),

    # COntact Form
    path('send_email/', views.sendEmail, name="send_email"),
]