from django.contrib import admin
from myapp.models import usuario, regalo, cancion, receta, pelicula, ciudad

# Register your models here.
class usuarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_usu','email_usu','celular_usu','fechanacimiento_usu']
    

class regaloAdmin(admin.ModelAdmin):
    list_display = ['id','usuario_reg', 'nombre_reg', 'descripcion_reg','url_reg']
    
class cancionAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_can', 'descripcion_can', 'url_can']
    
class recetaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_rec', 'categoria_rec', 'descripcion_rec', 'url_rec']

class peliculaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_pel', 'descripcion_pel', 'url_pel']
    
class ciudadAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_ciu', 'descripcion_ciu', 'url_ciu']

admin.site.register(usuario, usuarioAdmin)
admin.site.register(regalo, regaloAdmin )
admin.site.register(cancion, cancionAdmin)
admin.site.register(receta, recetaAdmin)
admin.site.register(pelicula, peliculaAdmin)
admin.site.register(ciudad, ciudadAdmin)

