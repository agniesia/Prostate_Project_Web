__author__ = 'Agnieszka'
from django.conf.urls import patterns, url, include


from django.contrib import admin
from profiles.forms import SignupFormExtra

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^accounts/signup/$','userena.views.signup',{'signup_form':SignupFormExtra }),
    url(r'^accounts/', include('userena.urls')),
)
