from gc import get_objects
from projects.serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
import os
from django.conf import settings
from django.shortcuts import get_object_or_404
# Para leer el modelo 
import json
from tensorflow.keras.models import load_model
from projects.views import funcion_modelo

MODEL_FILE=settings.MODEL_ROOT
IMAGENES_FILES=settings.MEDIA_FILES
modelo = load_model(MODEL_FILE+'/mix_model_low.h5')
ruta_imagenes = IMAGENES_FILES

class ProjectViewSet(viewsets.ModelViewSet):
    print("imprime resultado")
    # print(MODEL_FILE.mix_model_low.h5)
    # print(IMAGENES_FILES+'/')
    # print(funcion_modelo(modelo, ruta_imagenes,2,"Norte","Tienda"))
    # print(funcion_modelo(modelo, ruta_imagenes,2,"Norte","Tienda"))
    # funcion_modelo(modelo, ruta_imagenes,2,"Norte","Tienda")
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

    #anios_local,zona,tipo_tienda    
    def list(self, request, pk=None):
        print("ingresó aqui list")
        anios_local = request.query_params.get('anios_local')
        zona= request.query_params.get('zona')
        tipo_tienda = request.query_params.get('tipo_tienda')
        print(anios_local)
        print(zona)
        print(tipo_tienda)
    
        #print(self.funcion_modelo(2,"Norte","Tienda"))
        print(funcion_modelo(modelo, ruta_imagenes,int(anios_local),str(zona),str(tipo_tienda)))
        data=funcion_modelo(modelo, ruta_imagenes,int(anios_local),str(zona),str(tipo_tienda))
        serializer = ProjectSerializer(self.queryset, many=True)
        print(data[0][0])
        # result=json.dumps({'monto': data[0][0]})
        # print(result)
        return Response(data[0][0])

    def retrieve(self, request, pk=None):
        print("ingresó aqui retrive")
        #print(self.funcion_modelo(modelo, ruta_imagenes,2,"Norte","Tienda"))
        item = get_object_or_404(self.request, pk=pk)
        serializer = ProjectSerializer(item)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def items_not_done(self, request):
        print("ingresó aqui items_not_done")
        #print(self.funcion_modelo(modelo, ruta_imagenes,2,"Norte","Tienda"))
        projects = Project.objects.filter(done=False).count()

        return Response(projects)

    # def funcion_modelo(anios_local,zona,tipo_tienda):
    #     from tensorflow.keras.models import load_model
    #     MODEL_FILE=settings.MODEL_ROOT
    #     IMAGENES_FILES=settings.MEDIA_FILES
    #     modelo = load_model(MODEL_FILE+'/mix_model_low.h5')
    #     ruta_imagenes = IMAGENES_FILES
    #     import random
    #     import os
    #     import glob

    #     from tqdm import tqdm
    #     import pandas as pd
    #     pd.set_option('display.max_columns', None)
    #     from scipy.stats import variation

    #     import imageio as iio
    #     import cv2
    #     import skimage.measure    
    #     import pickle
    #     import numpy as np

    #     import tensorflow as tf
    #     from tensorflow import keras
    #     #from tensorflow.keras.preprocessing import image
    #     from tensorflow.keras.models import Model
    #     from tensorflow.keras import datasets, layers,models

    #     from keras import backend as K
    #     from tensorflow.keras.optimizers import Adam
    #     from sklearn.preprocessing import minmax_scale
    #     from tensorflow.keras.models import Sequential
    #     from tensorflow.keras.layers import BatchNormalization, Conv2D, MaxPooling2D, Activation, Dropout, Dense, Flatten, Input,InputLayer,Reshape
    #     from tensorflow.keras.layers import concatenate

    #     from sklearn.preprocessing import LabelEncoder
    #     from sklearn.preprocessing import MinMaxScaler

    #     from PIL import Image
    #     from PIL import ImageFilter


    #     def im_augmentation(value):
    #         size=256,256
    #         r = random.randrange(0, 7)

    #         if r == 0:
    #         # Rotacion
    #             return value.rotate(270)
    #         elif r == 1:
    #         # Zoom
    #             box = (50, 25, 200, 200)
    #             return value.crop(box).resize(size, resample=Image.BICUBIC)
    #         elif r == 2:
    #         # Filtros Intensidad
    #             return value.filter(ImageFilter.DETAIL)
    #         elif r == 3:
    #         # Rotacion
    #             return value.rotate(90)
    #         elif r == 4:
    #         # Filtros Intensidad
    #             return value.filter(ImageFilter.BLUR)
    #         elif r == 5:
    #         # Rotacion
    #             return value.rotate(180)
    #         else:
    #         # Filtros Intensidad
    #             return value.filter(ImageFilter.EDGE_ENHANCE)


    #     def collage_images(ruta_imagenes):
    #         size=255,255

    #         muestra = glob.glob(ruta_imagenes+"/*")

    #         if len(muestra) == 1:
    #             ima = Image.open(muestra[0]).resize(size, resample=Image.BICUBIC)

    #             # Horizontal concatenate 
    #             im1 = get_concat_h_resize(ima, im_augmentation(ima))
    #             im2 = get_concat_h_resize(im_augmentation(ima), im_augmentation(ima))

    #             # Vertical concatenate
    #             im_final = get_concat_v_resize(im1, im2)
                
    #             return im_final

    #         #    im_final.save(path+"/" +str(co)+".png")

    #         elif len(muestra) == 2:

    #             ima = Image.open(muestra[0]).resize(size, resample=Image.BICUBIC)
    #             imb = Image.open(muestra[1]).resize(size, resample=Image.BICUBIC)

    #             # Horizontal concatenate 
    #             im1 = get_concat_h_resize(ima, im_augmentation(imb))
    #             im2 = get_concat_h_resize(imb, im_augmentation(ima))

    #             # Vertical concatenate
    #             im_final = get_concat_v_resize(im1, im2)

    #             return im_final

    #         elif len(muestra) == 3:

    #             ima = Image.open(muestra[0]).resize(size, resample=Image.BICUBIC)
    #             imb = Image.open(muestra[1]).resize(size, resample=Image.BICUBIC)
    #             imc = Image.open(muestra[2]).resize(size, resample=Image.BICUBIC)
    #             # Selecciona imagen al azar
    #             imd = Image.open(muestra[random.randrange(0, 3)]).resize(size, resample=Image.BICUBIC)

    #             # Horizontal concatenate 
    #             im1 = get_concat_h_resize(im_augmentation(ima), imb)
    #             im2 = get_concat_h_resize(imc, ima)

    #             # Vertical concatenate
    #             im_final = get_concat_v_resize(im1, im2)

    #             return im_final

    #         else:
    #             r2 = random.sample(range(0, len(muestra)), 4)

    #             ima = Image.open(muestra[r2[0]]).resize(size, resample=Image.BICUBIC)
    #             imb = Image.open(muestra[r2[1]]).resize(size, resample=Image.BICUBIC)
    #             imc = Image.open(muestra[r2[2]]).resize(size, resample=Image.BICUBIC)
    #             imd = Image.open(muestra[r2[3]]).resize(size, resample=Image.BICUBIC)

    #             # Horizontal concatenate 
    #             im1 = get_concat_h_resize(im_augmentation(ima), imb)
    #             im2 = get_concat_h_resize(imc, imd)

    #             # Vertical concatenate
    #             im_final = get_concat_v_resize(im1, im2)

    #             return im_final


    #     def get_concat_h_resize(im1, im2,resample=Image.BICUBIC, resize_big_image=True):
    #         if im1.height == im2.height:
    #             _im1 = im1
    #             _im2 = im2
    #         elif (((im1.height > im2.height) and resize_big_image) or
    #                 ((im1.height < im2.height) and not resize_big_image)):
    #             _im1 = im1.resize((int(im1.width * im2.height / im1.height), im2.height), resample=resample)
    #             _im2 = im2
    #         else:
    #             _im1 = im1
    #             _im2 = im2.resize((int(im2.width * im1.height / im2.height), im1.height), resample=resample)
    #             dst = Image.new('RGB', (_im1.width + _im2.width, _im1.height))
    #             dst.paste(_im1, (0, 0))
    #             dst.paste(_im2, (_im1.width, 0))
    #             return dst

    #     def get_concat_v_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=True):
    #         if im1.width == im2.width:
    #             _im1 = im1
    #             _im2 = im2
    #         elif (((im1.width > im2.width) and resize_big_image) or
    #             ((im1.width < im2.width) and not resize_big_image)):
    #             _im1 = im1.resize((im2.width, int(im1.height * im2.width / im1.width)), resample=resample)
    #             _im2 = im2
    #         else:
    #             _im1 = im1
    #             _im2 = im2.resize((im1.width, int(im2.height * im1.width / im2.width)), resample=resample)
    #         dst = Image.new('RGB', (_im1.width, _im1.height + _im2.height))
    #         dst.paste(_im1, (0, 0))
    #         dst.paste(_im2, (0, _im1.height))
    #         return dst

    #     def cat_zona(value):
    #         if value == "Norte":
    #             return 1
    #         elif value == "Sur":
    #             return 2
    #         elif value == "Valles":
    #             return 3
    #         else:
    #             return 4


    #     def cat_tipo_tienda(value):
    #         if value == "Bodega de Abarrotes":
    #             return 0
    #         elif value == "Delicatessen":
    #             return 1
    #         elif value == "Frigorifico":
    #             return 2
    #         elif value == "Fruteria / Verduleria":
    #             return 3
    #         elif value == "Micromercado":
    #             return 4
    #         elif value == "Panaderia":
    #             return 5
    #         elif value == "Tienda":
    #             return 6
    #         else:
    #             return 7


    #     ['Bodega de Abarrotes', 'Delicatessen', 'Frigorífico','Frutería / Verdulería', 'Micromercado', 'Panadería', 'Tienda']
    #     ['Norte', 'Sur', 'Valles']

    #     collage = collage_images(ruta_imagenes)

    #     collage.save(ruta_imagenes+"/" +str(1)+".png")


    #     images = []
    #     image = cv2.imread(ruta_imagenes+"/" +str(1)+".png")
    #     image = cv2.resize(image, (255, 255))
    #     images.append(image)
            
    #     imagen = np.array(images)/255.0

    #     #  anio_local_max = 75
    #     anios_p = anios_local/75

    #     zona_p = cat_zona(zona)

    #     tipo_tienda_p = cat_tipo_tienda(tipo_tienda)

    #     X = []
    #     X.append([zona_p,tipo_tienda_p, anios_p])
    #     X = np.array(X)

    #     preds = modelo.predict([X, imagen])
    #     #ventas_max = 11282 
    #     preds=2200
    #     return preds*11282
        
