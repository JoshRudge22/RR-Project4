from django import forms
from .models import Profile, JobApplication, AvailableTime, NoticeTimes

class AvailableTimeForm(forms.ModelForm):
    class Meta:
        model = AvailableTime
        fields = ['time']