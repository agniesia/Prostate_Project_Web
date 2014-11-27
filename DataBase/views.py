from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from guardian.decorators import permission_required


@permission_required('auth.change_user')
def database(request):
    return render_to_response('project_info/database.html',{},context_instance=RequestContext(request))