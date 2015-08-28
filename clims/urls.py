from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from clims.views import *
from front import sample_views, sampletype_views, project_views, customer_views, barcode_views, status_views, species_views, storages_views, views

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/front/'

admin.site.site_header = 'CLIMS Administration'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'clims.views.user_login', name='login'),
    url(r'^front/$', include('front.urls', namespace="front", app_name='front')),
    url(r'^about/$', include('front.urls', namespace="about", app_name='about')),
    #url(r'^front/$', include('front.urls', namespace="front", app_name='front')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'), #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # sample upload
    url(r'^barcode/show/$', barcode_views.show),
    url(r'^customer/show/$', customer_views.show),
    url(r'^storage/show/$', storages_views.show),
    url(r'^project/show/$', project_views.show),
    url(r'^sample/show/$', sample_views.show),
    url(r'^sampletype/show/$', sampletype_views.show),
    url(r'^species/show/$', species_views.show),
    url(r'^status/show/$', status_views.show),
    url(r'^sample/delete/(?P<id>\d+)/$', sample_views.delete),

    # Serve static content.
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)
handler404 = "clims.views.handler404"
