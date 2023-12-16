from django.shortcuts import render, redirect
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from myapp.models import usuario, cancion, receta, regalo, pelicula, ciudad

# Create your views here.
# @login_required
def index(request):
    variable = "FIESTAS NAVIDEÑAS: Empieza la época de tradiciones, familia y regalos"
    context = {
        "variable": variable,
    }
    return render(request, 'myapp/index.html', context)

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

# @login_required
# def recetas_old(request):
#     condicion = True
#     variable = "*** FIESTAS NAVIDEÑAS - RECETAS ***"
#     my_plan = receta.objects.all()

#     context = {
#         "recetas1": my_plan,
#         "variable": variable,
#     }
#     return render(request, 'myapp/recetas.html', context)

@login_required
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

@login_required
def recetas(request):
    rega = receta.objects.all()
    variable = "*** FIESTAS NAVIDEÑAS - RECETAS ***"
    context = {
        "rega": rega,
        "variable": variable,

    }
    return render(request, 'myapp/recetas.html', context)


def recetas_create(request):
    mensaje = "*** FIESTAS NAVIDEÑAS - NUEVA RECETA ***"

    if request.method == 'POST':
        data_receta  = request.POST
        # definir los atributos del nuevo registro
        nombre = data_receta.get('nombre')
        decripcion =  data_receta.get('decripcion')
        categoria = "Navidad"
        sitio = data_receta.get('sitio')

        # crear el registro 
        rc = receta()
        rc.nombre_rec = nombre
        rc.descripcion_rec = decripcion
        rc.categoria_rec = categoria
        rc.url_rec = sitio
        rc.save()
        
        return redirect("app:recetas")

    context = {
        "rega": None,
        "mensaje": mensaje,
    }

    return render(request, 'myapp/recetas_create.html', context)


def recetas_detail(request, id_receta):
    rega = receta.objects.filter(id = id_receta).first()
    mensaje = "RECETAS - Detalle"
    context = {
        "rega": None,
        "mensaje": mensaje,
    }
    if rega:
        context["rega"] = rega

    return render(request, 'myapp/recetas_detail.html', context)

#def recets_import(request):
#     mensaje = "RECETAS - Import"

#     if request.method == 'POST':
#         receta_import_file = request.FILES["receta_import_file"]
#         # TODO: Agregar validacion sobre el archivo: ej: https://pythoncircle.com/post/30/how-to-upload-and-process-the-csv-file-in-django/

#         file_data = receta_import_file.read().decode("utf-8")
#         lines = file_data.split("\n")
#         for line in lines:
#             records_values = line.split(',')
#             receta = records_values[0]
#             decripcion = records_values[1]

#             rc = receta()
#             rc.nombre_rec = nombre
#             rc.descripcion_rec = decripcion
#             rc.categoria_rec = categoria
#             rc.url_rec = sitio
#             rc.save()

#         return redirect("app:recetas")

#     context = {
#         "rega": None,
#         "mensaje": mensaje,
#     }

#     return render(request, 'myapp/recetas_import.html', context)

