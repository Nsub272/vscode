from rest_framework import serializers
from .models import  Pais, Region, Provincia, Comuna, Direccion, Propiedad_Tipo, Estado_Propiedad, Autor, ubicacion, Usuario, Propiedad

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        #fields = '__all__' esta definicion trae todos los campos de la tabla
        fields = [ 'nombre_pais', 'nacionalidad', 'iso2', 'iso3']
        