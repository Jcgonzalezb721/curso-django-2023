from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index ),
    path('canciones', views.canciones ),
    path('recetas', views.recetas ),
    path('regalos', views.regalos ),
    path('peliculas', views.peliculas ),
    path('ciudades', views.ciudades ),
]
