from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login

#===============================================================================
# 
#===============================================================================
def index(request):
	return render_to_response('nueva_historia.djhtml', {}, 
						context_instance=RequestContext(request))

#===============================================================================
# 
#===============================================================================
def login_or_redirect(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect('')
	else:
		return login(request, kwargs)
	