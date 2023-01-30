from django.urls import path
from fastReading.views import upload
from aboutme.views import aboutmehome
from blog.views import BlogListView
from nutriplan.views import nutrihome
from landing import views


urlpatterns = [
    path('fastReading/upload', upload, name="fastReading/upload"),
    path('aboutme', aboutmehome, name="about_me_home"),
    path('', views.Tasks_lists.as_view(), name="home"),
    path('blog', BlogListView.as_view(), name="BlogListView"),
    path('nutriplan', nutrihome, name="nutrihome"),

    # COntact Form
    path('send_email/', views.sendEmail, name="send_email"),
]