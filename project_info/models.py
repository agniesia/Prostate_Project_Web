from django.db import models

# Create your models here.


class Publication(models.Model):
    list_of_authors = models.TextField()
    title = models.TextField()
    newspaper = models.TextField()

class Contributor(models.Model):
    names = models.CharField(max_length=30)
    title = models.CharField(max_length=15)
