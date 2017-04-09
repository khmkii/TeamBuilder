from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


def must_be_empty(value):
    if value:
        raise forms.ValidationError('Is not empty')


class SiteUserCreationForm(UserCreationForm):

    honey_pot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label='leave empty',
        validators=[must_be_empty]
    )

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
