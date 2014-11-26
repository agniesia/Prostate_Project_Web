from django.shortcuts import render, render_to_response
from guardian.decorators import permission_required
from project_info.models import Publication ,Contributor

# Create your views here.

#def about(request):
    #return render(request, 'project_info/about.html')

def publications(request):
    publications_paper = Publication.objects.all()
    return render_to_response('project_info/publications.html',{'publications':publications_paper})

def contact(request):
    list_of_contributors = Contributor.objects.all()
    return render_to_response('project_info/contact.html',{'contributors':list_of_contributors})

@permission_required('auth.change_user')
def database(request):
    return render_to_response('project_info/database.html',{})