from django.db import models
from django.utils import timezone

str_habilitado = "Habilitado"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_codigo = "Código"
str_nombre = "Nombre"
str_descripcion = "Descripción"
str_www = "WWW"
str_email = "Email"
str_telefono = "Teléfono"
str_fecha_nac = "Fecha Nacimiento"

class Pais(models.Model):
    nombre = models.CharField("País",max_length=50,null=False)
    nacionalidad = models.CharField("Nacionalidad",max_length=30,null=False)
    iso_2 = models.CharField("ISO 2",max_length=2,null=False)
    iso_3 = models.CharField("ISO 3",max_length=3,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Información de paises del mundo, para asociar a autores de Propiedad."

class Region(models.Model):
    codigo = models.CharField(str_codigo,max_length=2,null=False)
    region = models.CharField("Región",max_length=30,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Regiones de todo el mundo."

class Provincia(models.Model):
    codigo = models.CharField(str_codigo,max_length=3,null=False)
    provincia = models.CharField("Provincia",max_length=50,null=False)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Provincias de todo el mundo."

class Comuna(models.Model):
    codigo = models.CharField(str_codigo,max_length=5,null=False)
    comuna = models.CharField("Comuna",max_length=60,null=False)
    provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Comunas de todo el mundo."

class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=False)
    calle = models.CharField("Calle",max_length=100,null=True)
    numero = models.CharField("Número",max_length=10,null=True)
    departamento = models.CharField("Dpto/Oficina",max_length=10,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Direcciones de todo el mundo."

class Autor(models.Model):
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    descripcion = models.TextField(str_descripcion,null=True)
    www = models.URLField(str_www,max_length=200,null=True)
    email = models.EmailField(str_email,max_length=100,null=True)
    telefono = models.CharField(str_telefono,max_length=20,null=True)
    fecha_nacimiento = models.DateField(str_fecha_nac,null=True)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Autores de Propiedades."

Propiedad_Tipo = [
    ('Casa', 'Casa'),
    ('Departamento', 'Departamento'),
    ('Oficina', 'Oficina'),
    ('Local Comercial', 'Local Comercial'),
    ('Terreno', 'Terreno'),]

class Estado_Propiedad(models.Model):
    nombre = models.CharField(str_nombre,max_length=50,null=False)
    descripcion = models.TextField(str_descripcion,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Estados de Propiedades, como Disponible, Vendida, Alquilada, etc."

class Propiedad(models.Model):
    # Se añade null=True, blank=True a los campos nuevos para evitar errores en registros antiguos
    nombre = models.CharField(str_nombre,max_length=100,null=True, blank=True)
    descripcion = models.TextField(str_descripcion,null=True, blank=True)
    tipo = models.CharField("Tipo",max_length=20,choices=Propiedad_Tipo,null=True, blank=True)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True, blank=True)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,null=True, blank=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True,null=True)
    estado_Propiedad = models.ForeignKey(Estado_Propiedad, on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True,null=True)
    class Meta:
        db_table_comment = "Propiedades de todo el mundo."

class ubicacion(models.Model):
    propiedad = models.ForeignKey(Propiedad,on_delete=models.CASCADE,null=False)
    latitud = models.DecimalField("Latitud",max_digits=9, decimal_places=6,null=False)
    longitud = models.DecimalField("Longitud",max_digits=9, decimal_places=6,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Ubicación de Propiedades en el mapa."

class Usuario(models.Model):
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    email = models.EmailField(str_email,max_length=100,null=False,unique=True)
    telefono = models.CharField(str_telefono,max_length=20,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Usuarios del sistema de gestión inmobiliaria."