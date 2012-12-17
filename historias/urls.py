from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('historias_medicas.urls')),
    url(r'^login$', login, {'template_name': 'login.djhtml'}, name='login'),
    # Examples:
    # url(r'^$', 'historias.views.home', name='home'),
    # url(r'^historias/', include('historias.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
