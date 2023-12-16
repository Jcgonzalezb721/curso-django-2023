from django.contrib import admin
from django.urls import path, include
from myapp import views

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('canciones', views.canciones, name='canciones'), 
    path('recetas', views.recetas, name='recetas'), 
    path('recetas/<int:id_receta>', views.recetas_detail, name='recetas' ),
    path('recetas/create/', views.recetas_create, name='recetas_create' ),
    # path('resetas/import/', views.recetas_import, name='recetas_import' ),
    path('regalos', views.regalos, name='regalos'), 
    path('peliculas', views.peliculas, name='peliculas'),     
    path('ciudades', views.ciudades, name='ciudades'),     
]
