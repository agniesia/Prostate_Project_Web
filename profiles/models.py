from django.db import models
from django.utils.translation import ugettext_lazy as _
from userena.models import UserenaLanguageBaseProfile
from userena.utils import user_model_label

class InstitutionMailOnly(UserenaLanguageBaseProfile):
    """ Custom profile """

    #hack for related_name='profile' used in forms
    user = models.OneToOneField(user_model_label,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')

    #hack the same name 'Institution' for custom model and form
    Institution = models.CharField(max_length=60)




