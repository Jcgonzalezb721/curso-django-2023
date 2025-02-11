from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from myapp.models import usuario, cancion, receta, regalo, pelicula, ciudad

# Create your views here.
@login_required
def index(request):
    variable = "FIESTAS NAVIDEÑAS: Empieza la época de tradiciones, familia y regalos"
    context = {
        "variable": variable,
    }
    return render(request, 'myapp/index.html', context)

@login_required
def canciones(request):
    condicion = True
    variable = "*** FIESTAS NAVIDEÑAS - CANCIONES ***"
    my_plan = cancion.objects.all()


    # for cl in my_plan:
    #     # your code is here 
    #     print(ln)

    context = {
        "canciones": my_plan,
        "variable": variable,
    }
    return render(request, 'myapp/canciones.html', context)

@login_required
def recetas(request):
    condicion = True
    variable = "*** FIESTAS NAVIDEÑAS - RECETAS ***"
    my_plan = receta.objects.all()

    context = {
        "recetas": my_plan,
        "variable": variable,
    }
    return render(request, 'myapp/recetas.html', context)

def regalos(request):
    condicion = True
    variable = "*** FIESTAS NAVIDEÑAS - REGALOS ***"
    my_plan = regalo.objects.all()

    context = {
        "regalos": my_plan,
        "variable": variable,
    }
    return render(request, 'myapp/regalos.html', context)


def peliculas(request):
    condicion = True
    variable = "*** FIESTAS NAVIDEÑAS - PELICULAS ***"
    my_plan = pelicula.objects.all()

    # for cl in my_plan:
    #     # your code is here 
    #     print(cl)
    context = {
        "peliculas": my_plan,
        "variable": variable,
    }
    return render(request, 'myapp/peliculas.html', context)

def ciudades(request):
    condicion = True
    variable = "*** FIESTAS NAVIDEÑAS - CIUDADES ***"
    my_plan = ciudad.objects.all()

    context = {
        "ciudades": my_plan,
        "variable": variable,
    }
    return render(request, 'myapp/ciudades.html', context)

