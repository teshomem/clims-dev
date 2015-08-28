from django.conf.urls import patterns, url

#from front import views, sample_views
from front import views, species_views

urlpatterns = patterns('',
    #url(r'^$', species_views.show),
    url(r'^$', views.about),
)
