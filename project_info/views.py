from django.shortcuts import render, render_to_response
from django.template import RequestContext
from guardian.decorators import permission_required
from project_info.models import Publication ,Contributor, Contact

# Create your views here.

#def about(request):
    #return render(request, 'project_info/about.html')

def publications(request):
    publications_paper = Publication.objects.all()
    return render_to_response('project_info/publications.html',{'publications':publications_paper},context_instance=RequestContext(request))

def contact(request):
    list_of_contributors = Contributor.objects.all()
    contact_info = Contact.objects.all()[0]
    return render_to_response('project_info/contact.html',{'contact_info': contact_info,'contributors':list_of_contributors},context_instance=RequestContext(request))

@permission_required('auth.change_user')
def database(request):
    return render_to_response('project_info/database.html',{},context_instance=RequestContext(request))