__author__ = 'Agnieszka'
from django.conf.urls import patterns, url
from project_info.models import Publication
from  django.contrib.flatpages import  views
urlpatterns = patterns('',

                       url(r'^publications/$','project_info.views.publications', name='publications'),
                       url(r'^contact/$','project_info.views.contact',name='contact'),
                       url(r'^database/$','project_info.views.database',name='database'),
                       )