# -*- coding: utf-8 -*-

from django.db import models

class Persona(models.Model):
	cedula				= models.CharField(max_length=10, unique=True)
	nombre   			= models.CharField(max_length=30)
	apellido			= models.CharField(max_length=30)
	fecha_nacimiento	= models.DateField()
	direccion			= models.TextField(blank=True)
	telefono_casa		= models.CharField(max_length=20, blank=True)
	telefono_celular	= models.CharField(max_length=20, blank=True)

	class Meta:
		verbose_name = u'Persona'
		verbose_name_plural = u'Personas'

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
	peso  			= models.DecimalField(max_digits=5, decimal_places=2)
	talla			= models.IntegerField()
	tension			= models.CharField(max_length=15)
	pulso			= models.IntegerField()
	diagnostico 	= models.TextField()
	tratamiento 	= models.TextField()
	pendiente		= models.TextField(blank=True)

	class Meta:
		verbose_name = u'Historia'
		verbose_name_plural = u'Historias' 

	def __unicode__(self):
		return u"{} - ({})".format(self.persona.cedula, self.fecha)

class TipoExamen(models.Model):
	"""
	Un tipo de examen en especifico. Ej. "Cuenta y Fórmula", "Rayos X"
	"""
	nombre = models.CharField(max_length=25, unique=True)

	class Meta:
		verbose_name = u'Tipo de Examen'
		verbose_name_plural = u'Tipo de examenes'

	def __unicode__(self):
		return self.nombre

class CampoExamen(models.Model):
	"""
	Un campo especifico de un examen con su nombre y 
	tipo de datos
	"""
	# Constants
	INT 	= "int"
	REAL 	= "real"
	STRING 	= "string"
	TIPO_DATO_CHOICES = (
		(INT, "Entero"),
		(REAL, "Decimal"),
		(STRING, "Texto")
	)

	# Model variables
	nombre 		= models.CharField(max_length=20, unique=True)
	tipo_examen	= models.ForeignKey('TipoExamen', related_name='campos')
	tipo_datos	= models.CharField(max_length=15, 
		choices=TIPO_DATO_CHOICES, default=STRING
	)
	unidad		= models.CharField(max_length=25, blank=True)

	class Meta:
		verbose_name = u'Campo'
		verbose_name_plural = u'Campos'

	def __unicode__(self):
		return u"{}: {} ({})".format(self.tipo_examen.__unicode__(),
			self.nombre, self.tipo_datos
		)

class ResultadoExamen(models.Model):
	"""
	Mantiene los resultados de un examen especifico dentro
	de una historia
	"""
	historia 	= models.ForeignKey('Historia', related_name='examenes')
	tipo_examen	= models.ForeignKey('TipoExamen')

	class Meta:
		verbose_name = u'Restulado de Examen'
		verbose_name_plural = u'Resultados de Examen'

	def __unicode__(self):
		return u"Historia: {} Tipo Examen: {}".format(self.historia.__unicode__(),
			self.tipo_examen.__unicode__()
		)

class ResultadoCampoExamen(models.Model):
	"""
	Resultado de un campo de un examen en especifico
	"""
	resultado_examen 	= models.ForeignKey('ResultadoExamen', related_name='campos')
	campo_examen		= models.ForeignKey('CampoExamen')
	valor 				= models.CharField(max_length=25)
	nota				= models.TextField()

	class Meta:
		verbose_name = u'Resultado Campo Examen'
		verbose_name_plural = u'Resultados de Campo de Examen'

	def __unicode__(self):
		return u'{} {} {} {}'.format(self.resultado_examen.__unicode__(),
			self.campo_examen.__unicode__(), self.valor, self.nota
		)


