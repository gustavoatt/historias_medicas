import datetime

import django.forms
import django.forms.extras as extras

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import AppendedText

from historias_medicas import models


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

	def __init__(self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)
		
		# Django-crispy-forms helper so that they are rendered correctly
		self.helper = FormHelper(self)
		self.helper.form_class = 'form-horizontal'
		self.helper.form_tag = True
		self.helper.form_id = 'nueva_persona_form'
		self.helper.form_action = 'nueva_persona'

		self.helper.form_show_errors = True
		self.helper.error_text_inline = False

		self.helper.add_input(Submit('crear', 'Crear'))


class HistoriaForm(django.forms.ModelForm):
	class Meta:
		model = models.Historia

	def __init__(self, *args, **kwargs):
		super(HistoriaForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		self.helper.form_class = 'form-horizontal'
		self.helper.form_tag = True
		self.helper.form_id = 'nueva_historia_form'
		self.helper.form_action = 'nueva_historia'

		self.helper.form_show_errors = True
		self.helper.error_text_inline = False
		self.helper.add_input(Submit('crear', 'Crear'))
		self.helper['peso'].wrap(AppendedText, "peso", "kg")
		self.helper['talla'].wrap(AppendedText, "talla", "m")