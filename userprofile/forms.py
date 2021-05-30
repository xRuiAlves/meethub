from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Profile


class UserForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
