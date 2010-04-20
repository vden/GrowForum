from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request, day=None, month=None, year=None):
	# some code to get posts/articles/etc by
	# passed day, month or year
	
	return render_to_response("archive/index.html", {}, context_instance=RequestContext(request))

