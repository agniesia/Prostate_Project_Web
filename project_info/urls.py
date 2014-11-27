__author__ = 'Agnieszka'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^publications/$','project_info.views.publications', name='publications'),
                       url(r'^contact/$','project_info.views.contact',name='contact'),
                       )