#python
import tensorflow as tf

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
import cv2
from PIL import Image
#django
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,)

@api_view(['GET'])
def saludar(request):
    return JsonResponse({'hola':'https://web-production-1728.up.railway.app/media/img_0.jpg'})

@api_view(['GET'])
def get_image(request):
    # Devolver la ruta de la imagen generada como respuesta HTTP
    return JsonResponse({'imagen': 'https://web-production-1728.up.railway.app/media/img_0.jpg'})

@api_view(['POST'])
def create_image(request):
     # Cargamos el modelo Inception entrenado, para obtener más información sobre el aprendizaje de transferencia, consulte los casos de estudio anteriores
    base_model = tf.keras.applications.InceptionV3(include_top = False, weights = 'imagenet')
    #%%
    # Abrir la primera imagen
    # Fuente: https://www.pxfuel.com/en/free-photo-xxgfs
   # img_1 = Image.open("./imagenes/p1.jpeg")
    image1 = request.data['image1']
    image2 = request.data['image2']

    width = 640
    height = 480

    # Cargar las imágenes con Pillow (PIL)
    pil_image1 = Image.open(image1)
    pil_image2 = Image.open(image2)

    # Redimensionar las imágenes al tamaño deseado
    resized_image1 = pil_image1.resize((width, height))
    resized_image2 = pil_image2.resize((width, height))


    # Guardar las imágenes procesadas
    processed_image1_path = "./media/001.jpg"
    processed_image2_path = "./media/002.jpg"
    resized_image1.save(processed_image1_path)
    resized_image2.save(processed_image2_path)

    img_1 = Image.open("./media/001.jpg")
    img_2 = Image.open("./media/002.jpg")

    # Abrir la segunda imagen
    # Fuente: https://commons.wikimedia.org/wiki/File:Georges_Garen_embrasement_tour_Eiffel.jpg
   # img_2 = Image.open('./imagenes/p2.jpeg')

    # Fusionar ambas imágenes

    image = Image.blend(img_1, img_2, 0.6) # alpha --> El factor alfa de interpolación. Si alfa es 0.0, se devuelve una copia de la primera imagen.
    # Si alpha es 1.0, se devuelve una copia de la segunda imagen.

    # Guardamos la mezcla
    image.save("./media/img_0.jpg")
    
    return JsonResponse({'hola':'mundo'})
