__author__ = 'Agnieszka'
from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupFormOnlyEmail

class SignupFormExtra(SignupFormOnlyEmail):
    """
    A form to demonstrate how to add extra fields to the signup form, in this
    case adding the first and last name.


    """

    Institution = forms.CharField(label=_(u'Institution'),
                                max_length=60,
                                required=False)

    def __init__(self, *args, **kw):
        """

        A bit of hackery to get the first name and last name at the top of the
        form instead at the end.

        """
        super(SignupFormExtra, self).__init__(*args, **kw)

    def save(self):
        user = super(SignupFormExtra, self).save()

        # Get the profile, the `save` method above creates a profile for each
        # user because it calls the manager method `create_user`.
        # See: https://github.com/bread-and-pepper/django-userena/blob/master/userena/managers.py#L65
        #My hack for django v=1.7.1

        user_profile = user.profile

        # Be sure that you have validated these fields with `clean_` methods.
        # Garbage in, garbage out.
        user_profile.Institution = self.cleaned_data['Institution']

        user_profile.save()


        return user