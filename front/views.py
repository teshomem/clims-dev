#from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
# new added
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

#@login_required
def front_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render(request, 'front/index.html')

#@login_required
def about(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render(request, 'front/about.html')

def handler404(request):
    return render(request, '404.html')
