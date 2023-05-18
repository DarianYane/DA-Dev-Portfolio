from rest_framework import routers
from .api import JobViewSet

router = routers.DefaultRouter()

router.register('api/jobs', JobViewSet, 'jobs')

urlpatterns = router.urls