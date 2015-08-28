from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from front.models import Status 
import front.forms
import datetime
from django.forms.models import modelformset_factory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

@login_required
def show(request):
    return render(request, 'status/show.html', {'obj': Status.objects.all().order_by('-id')[:10]})

@login_required
def FrontDisplay(request):
    status = Status.objects.get(id=1)
    return render(request, 'status/show.html', {'obj': Status.objects.all()})

def delete(request):
    """Deletes a Status and corresponding dependencies"""
    status = Status.objects.get(id = int(request.REQUEST['id']))
    status.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')
