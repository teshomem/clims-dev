from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from front.models import Species 
import front.forms
import datetime
from django.forms.models import modelformset_factory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

@login_required
def show(request):
    return render(request, 'species/show.html', {'obj': Species.objects.all().order_by('-id')[:10]})

@login_required
def FrontDisplay(request):
    species = Species.objects.get(id=1)
    return render(request, 'species/show.html', {'obj': Species.objects.all()})

def delete(request):
    """Deletes a Species and corresponding dependencies"""
    species = Species.objects.get(id = int(request.REQUEST['id']))
    species.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')
