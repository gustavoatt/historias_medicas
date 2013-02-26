from views import index, crear_persona, crear_historia
from django.conf.urls import patterns, url
from django.contrib.auth.views import login

urlpatterns = patterns('',
	url(r'^$', index, name='home'),
	url(r'^login$', login, {'template_name': 'login.djhtml'}, name='login'),
	url(r'^nueva_persona', crear_persona, name='nueva_persona'),
	url(r'^nueva_historia', crear_historia, name='nueva_historia'),
)