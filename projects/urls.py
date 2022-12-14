from rest_framework import routers
from django.urls import path
from .api import ProjectViewSet
from projects.views import resultModelo

router = routers.DefaultRouter()

# router.register('api/projects/modelo', ProjectViewSet, 'projects') 

# router.register('api/projects/modelo/', ProjectViewSet.as_view({
#     'get':'list',
# }), 'projects') 
# router.register('api/projects/modelo/', views.funcion_modelo, 'projects') 

# router.register('api/projects/modelos/', ProjectViewSet.as_view({
#     'get':'getModelo'
# }), 'projects')



# urlpatterns = router.urls

urlpatterns = [
     path('api/projects/modelo', ProjectViewSet.as_view({
        'get':'list'
     }), name='projects'),
     path('api/imagenes', resultModelo, name='modelo')
]




