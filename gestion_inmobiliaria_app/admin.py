from django.contrib import admin
from .models import  Pais, Region, Provincia, Comuna, Direccion, Propiedad_Tipo, Estado_Propiedad, Autor, ubicacion, Usuario, Propiedad
# Register your models here.
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Propiedad_Tipo)
admin.site.register(Estado_Propiedad)
admin.site.register(Autor)
admin.site.register(ubicacion)
admin.site.register(Usuario)
admin.site.register(Propiedad)

