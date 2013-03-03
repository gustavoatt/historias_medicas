from django.db import models

class Persona(models.Model):
	cedula				= models.CharField(max_length=10, unique=True)
	nombre   			= models.CharField(max_length=30)
	apellido			= models.CharField(max_length=30)
	fecha_nacimiento	= models.DateField()
	direccion			= models.TextField(blank=True)
	telefono_casa		= models.CharField(max_length=20, blank=True)
	telefono_celular	= models.CharField(max_length=20, blank=True)

	def __unicode__(self):
		return "({}) {} {}".format(self.cedula, 
		                          self.apellido, 
		                          self.nombre)

	@models.permalink
	def get_absolute_url(self):
		return ('historias_de_paciente', [self.id])

class Historia(models.Model):
	persona			= models.ForeignKey('Persona', 
	                              blank=False, 
	                              null=True,
	                              related_name='historias')
	fecha 			= models.DateTimeField(unique=True, 
	                            auto_now_add=True)
	motivo 			= models.TextField()
	peso  			= models.DecimalField(blank=True,
	                               max_digits=5, decimal_places=2)
	talla			= models.IntegerField(blank=True)
	tension			= models.CharField(max_length=15)
	pulso			= models.IntegerField()
	diagnostico 	= models.TextField()
	tratamiento 	= models.TextField()
	pendiente		= models.TextField(blank=True)
