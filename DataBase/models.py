from django.db import models

# Create your models here.

class CTDataOneAcquisitionForPatient(models.Model):
    share_link = models.TextField()

class MRICTData(models.Model):
    share_link = models.TextField()

class CTDataMoreAcquisitionForPatient(models.Model):
    share_link = models.TextField()