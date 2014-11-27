from django.conf.urls import patterns, url

__author__ = 'Agnieszka'

urlpatterns = patterns('',
                       url(r'^database/$','project_info.views.database',name='database'),
                       )