from django.contrib import admin
from models import CTDataMoreAcquisitionForPatient, CTDataOneAcquisitionForPatient, MRICTData
# Register your models here.


class CTDataMoreAcquisitionForPatientAdmin(admin.ModelAdmin):
    pass


class CTDataOneAcquisitionForPatientAdmin(admin.ModelAdmin):
    exclude = ()


class MRICTDataAdmin(admin.ModelAdmin):
    exclude = ()



admin.site.register(MRICTData,MRICTDataAdmin)
admin.site.register(CTDataOneAcquisitionForPatient,CTDataOneAcquisitionForPatientAdmin)
admin.site.register(CTDataMoreAcquisitionForPatient,CTDataMoreAcquisitionForPatientAdmin)