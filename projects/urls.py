from rest_framework import routers
from django.urls import path
from .api import ProjectViewSet
from projects import views

router = routers.DefaultRouter()

router.register('api/projects/modelo', views, 'projects') 

# router.register('api/projects/modelos', ProjectViewSet.as_view({
#     'get':'getModelo'
# }), 'projects')



urlpatterns = router.urls

# urlpatterns = [
#      path('modelo/', getModelo, name='modelo')
# ]




