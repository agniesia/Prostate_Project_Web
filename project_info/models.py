from django.contrib.flatpages.models import FlatPage
from django.db import models

# Create your models here.


class Publication(models.Model):
    list_of_authors = models.TextField()
    title = models.TextField()
    newspaper = models.TextField()


class Contributor(models.Model):
    names = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    function = models.CharField(max_length=30,blank=True )


class Contact(models.Model):
    contact_name = models.CharField(max_length=40)
    contact_email = models.EmailField()
    telephone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    project_email = models.EmailField()
    institutions = models.TextField()
    map = models.ImageField()



    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Contact, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()






