import models

import django.views.generic.list  as django_list_views
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required


from historias_medicas import forms

#===============================================================================
# Welcome Page
#===============================================================================
def index(request):
	return render_to_response('base.djhtml', {}, 
	                          context_instance=RequestContext(request))

def login_or_redirect(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect('')
	else:
		return login(request, kwargs)

#===============================================================================
# Subclass of the generic view to show all the patients
#===============================================================================
class PacienteListView(django_list_views.ListView):
	model = models.Persona
	template_name = 'pacientes_view.djhtml'
	context_object_name = 'pacientes'

class HistoriaListView(django_list_views.ListView):
	template_name = 'show_historias.djhtml'
	context_object_name = 'historias'

	def get_queryset(self):
		self.persona = get_object_or_404(models.Persona, id=self.args[0])
		return models.Historia.objects.filter(persona=self.persona)

	def get_context_data(self, **kwargs):
		context = super(HistoriaListView, self).get_context_data(**kwargs)
		context['persona'] = self.persona

		return context
		
	
#===============================================================================
# Adds a new patient
#===============================================================================
@login_required
def crear_persona(request, **kwargs):
	if request.method == 'POST':
		form = forms.PersonaForm(request.POST)
		if form.is_valid():
			form.save()
			## CHANGE IT ###########################
			return HttpResponseRedirect('pacientes')
	else:
		form = forms.PersonaForm()
	
	return render_to_response('nueva_persona.djhtml', 
	                          {'form': form}, 
	                          context_instance=RequestContext(request)
	                          )


#===============================================================================
#
#===============================================================================
@login_required
def crear_historia(request, **kwargs):
	if request.method == 'POST':
		form = forms.HistoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(form.instance.persona)
	else:
		form = forms.HistoriaForm()

	return render_to_response('nueva_historia.djhtml',
	                          {'form': form},
	                          context_instance=RequestContext(request)
	                          )


