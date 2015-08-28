from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from front.models import Sampletype 
import front.forms
import datetime
from django.forms.models import modelformset_factory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

@login_required
def show(request):
    return render(request, 'sampletype/show.html', {'obj': Sampletype.objects.all().order_by('-id')[:10]})

@login_required
def FrontDisplay(request):
    sampletype = Sampletype.objects.get(id=1)
    return render(request, 'sampletype/show.html', {'obj': Sampletype.objects.all()})

def delete(request):
    """Deletes a Sampletype and corresponding dependencies"""
    sampletype = Sampletype.objects.get(id = int(request.REQUEST['id']))
    sampletype.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')
