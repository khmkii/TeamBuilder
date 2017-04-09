from django import forms
from django.contrib.auth import get_user_model


from . import models


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = [
            'first_name', 'middle_name', 'last_name', 'avatar',
            'story',
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProfileEditForm, self).__init__(*args, **kwargs)