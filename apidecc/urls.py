from rest_framework import routers
from .api import JobViewSet, DepartmentViewSet

router = routers.DefaultRouter()

router.register('api/jobs', JobViewSet, 'jobs')
router.register('api/departments', DepartmentViewSet, 'departments')

urlpatterns = router.urls