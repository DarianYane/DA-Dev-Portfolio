from rest_framework import routers
from .api import JobViewSet, DepartmentViewSet, HiredEmployeeViewSet

router = routers.DefaultRouter()

router.register('api/jobs', JobViewSet, 'jobs')
router.register('api/departments', DepartmentViewSet, 'departments')
router.register('api/hired-employees', HiredEmployeeViewSet, 'hired-employees')

urlpatterns = router.urls