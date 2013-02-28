import datetime

import django.forms
import django.forms.extras as extras

from historias_medicas import models
import widgets

class PersonaForm(django.forms.ModelForm):
	class Meta:
		model 	= models.Persona
		fields 	= ('cedula', 'nombre', 'apellido', 'fecha_nacimiento', 
		           'telefono_casa', 'telefono_celular', 'direccion')
		widgets = {
			'fecha_nacimiento': 
				extras.SelectDateWidget(years=range(1900, datetime.date.today().year + 1),
				                        attrs={
				                        	'class': 'span1'
				                        })
		}

class HistoriaForm(django.forms.ModelForm):
	class Meta:
		model = models.Historia
		widgets = {
			'peso': widgets.AppendedInput("kg",
			                              attrs={
			                              	'placeholder': "Peso",
			                              }),
			'talla': widgets.AppendedInput("cm", 
			                               attrs={
			                               	'placeholder': "Talla",
			                               })
		}