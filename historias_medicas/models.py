from django.db import models

class Persona(models.Model):
	cedula   					= models.CharField(max_length=10, unique=True)
	nombre   					= models.CharField(max_length=30)
	apellido   				= models.CharField(max_length=30)
	fecha_nacimiento 	= models.DateField()
	direccion					= models.TextField(blank=True)
	telefono_casa			= models.CharField(max_length=20, blank=True)
	telefono_celular	= models.CharField(max_length=20, blank=True)

class Historia(models.Model):
	fecha 			= models.DateField(auto_now_add=True)
	motivo 			= models.TextField()
	peso  			= models.IntegerField(blank=True)
	talla				= models.IntegerField(blank=True)
	tension			= models.CharField(max_length=15)
	pulso				= models.IntegerField()
	diagnostico = models.TextField()
	tratamiento = models.TextField()
	pendiente		= models.TextField(blank=True)
