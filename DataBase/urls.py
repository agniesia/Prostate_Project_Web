from django.conf.urls import patterns, url

__author__ = 'Agnieszka'

urlpatterns = patterns('',
                       url(r'^database/$','DataBase.views.database',name='database'),
                       )