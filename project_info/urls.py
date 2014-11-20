__author__ = 'Agnieszka'
from django.conf.urls import patterns, url
from project_info.models import Publication

urlpatterns = patterns('',
                       url(r'^about/$','project_info.views.about'),
                       url(r'^publications/$','project_info.views.publications'),
                       url(r'^contact/$','project_info.views.contact'),
                       url(r'^database/$','project_info.views.database'),
                       )