from rest_framework import routers
from django.urls import path
from .api import ProjectViewSet
from projects.views import getModelo

router = routers.DefaultRouter()

# router.register('api/projects', ProjectViewSet, 'projects') 

router.register('api/projects/modelos', ProjectViewSet.as_view({
    'get': 'getModelo'
}), 'projects')



urlpatterns = router.urls

# urlpatterns = [
#      path('modelo/', getModelo, name='modelo')
# ]




