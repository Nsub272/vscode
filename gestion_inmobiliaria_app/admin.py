from django.contrib import admin

# Importamos todos los modelos desde nuestro archivo models.py
from .models import (
    Pais, 
    Region, 
    Provincia, 
    Comuna, 
    Direccion, 
    Autor, 
    Estado_Propiedad, 
    Propiedad, 
    ubicacion, 
    Usuario
)

# Registramos los modelos para que aparezcan en el panel de administración
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Autor)
admin.site.register(Estado_Propiedad)
admin.site.register(Propiedad)
admin.site.register(ubicacion)
admin.site.register(Usuario)