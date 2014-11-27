from django.contrib import admin

# Register your models here.
from project_info.models import Publication, Contributor, Contact

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title','list_of_authors' ,'newspaper')
    search_fields = ['title','list_of_authors' ,'newspaper']
class ContributorsAdmin(admin.ModelAdmin):
    list_display = ('names','title','function')
    search_fields = ['title','names','function']

class ContactAdmin(admin.ModelAdmin):
    exclude = ()





admin.site.register(Publication,PublicationAdmin)
admin.site.register(Contributor,ContributorsAdmin)
admin.site.register(Contact,ContactAdmin)