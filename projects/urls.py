from rest_framework import routers

from .api import ProjectViewSet


router = routers.DefaultRouter()

# router.register('api/projects', ProjectViewSet, 'projects') 

router.register('api/projects/modelos', ProjectViewSet.list, 'projects')

urlpatterns = router.urls



