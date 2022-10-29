from projects.serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets, permissions
import modelo_mixto

class ProjectViewSet(viewsets.ModelViewSet):
    print(modelo_mixto)
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer