from apidecc.models import Job
from rest_framework import viewsets, permissions
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JobSerializer