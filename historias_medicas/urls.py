from views import index
from django.conf.urls import patterns, url
from django.contrib.auth.views import login

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^login$', login, {'template_name': 'login.djhtml'}, name='login'),
)