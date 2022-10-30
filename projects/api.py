from projects.serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
import os
from django.conf import settings
# Para leer el modelo
# import pickle
from tensorflow.keras.models import load_model

MODEL_FILE=settings.MODEL_ROOT
IMAGENES_FILES=settings.MEDIA_FILES
modelo = load_model(MODEL_FILE+'/mix_model_low.h5')
ruta_imagenes = IMAGENES_FILES+'/'
class ProjectViewSet(viewsets.ModelViewSet):
    print("imprime resultado")
    # print(MODEL_FILE.mix_model_low.h5)
    print(IMAGENES_FILES+'/')
    # funcion_modelo(modelo, ruta_imagenes,2,"Norte","Tienda")
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

    