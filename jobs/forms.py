from django import forms
from .models import Profile, AvailableTime, JobApplication

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 

class AvailableTimeForm(forms.ModelForm):
    class Meta:
        model = AvailableTime
        fields = ['time']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
        