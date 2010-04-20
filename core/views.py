from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	return render_to_response("core/index.html", {}, context_instance=RequestContext(request))

def help(request):
	return render_to_response("core/help.html", {}, context_instance=RequestContext(request))

def rules(request):
	return render_to_response("core/rules.html", {}, context_instance=RequestContext(request))

def growFaq(request):
	return render_to_response("core/grow_faq.html", {}, context_instance=RequestContext(request))
