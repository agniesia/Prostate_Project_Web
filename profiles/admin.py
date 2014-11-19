__author__ = 'Agnieszka'

from django.contrib import admin
from userena.admin import UserenaAdmin
from django.contrib.auth.models import User

from profiles.models import InstitutionMailOnly

class UserProfileInline(admin.TabularInline):
    model = InstitutionMailOnly

class UserAdmin(UserenaAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)