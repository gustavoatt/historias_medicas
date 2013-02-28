import models

import django.views.generic.list  as django_list_views
from django.shortcuts import render_to_response
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
			return HttpResponseRedirect('/thanks')
	else:
		form = forms.HistoriaForm()

	return render_to_response('nueva_historia.djhtml',
	                          {'form': form},
	                          context_instance=RequestContext(request)
	                          )


