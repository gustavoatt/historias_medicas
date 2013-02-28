import views

import django.contrib.auth  as django_auth
from django.conf.urls import patterns, url


urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^login$', django_auth.views.login, 
	    {'template_name': 'login.djhtml'}, 
	    name='login'
	),
	# Views that create new information
	url(r'^nueva_persona', views.crear_persona, 
	    name='nueva_persona'
	),
	url(r'^nueva_historia', views.crear_historia,
	    name='nueva_historia'
	),
	# Views that show information
	url(r'^pacientes', django_auth.decorators.login_required(views.PacienteListView.as_view()),
	    name='lista_pacientes'),
	
)