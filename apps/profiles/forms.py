from django import forms
from apps.profiles.models import Profile


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone', 'photo', 'sex', )
