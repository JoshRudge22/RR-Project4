from django import forms
from .models import Profile, AvailableTime

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 

class AvailableTimeForm(forms.ModelForm):
    class Meta:
        model = AvailableTime
        fields = ['time']