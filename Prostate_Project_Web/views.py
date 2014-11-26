__author__ = 'Agnieszka'
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import  HttpResponse

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def handler400(request):
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response

def index(request):

    return render(request, 'static\index.html')