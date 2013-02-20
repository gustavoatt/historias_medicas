from django.forms import ModelForm

from historias_medicas.models import Persona, Historia

class PersonaForm(ModelForm):
	class Meta:
		model 	= Persona
		fields 	= ('cedula', 'nombre', 'apellido', 'fecha_nacimiento', 
							'telefono_casa', 'telefono_celular', 'direccion')

class HistoriaForm(ModelForm):
	class Meta:
		model = Historia