from django import forms
from .models import ContactUsForm, Hiring


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUsForm
        fields = '__all__'


class HiringForm(forms.ModelForm):
    class Meta:
        model = Hiring
        fields = '__all__'
        widgets = {
            'job_description': forms.TextInput(attrs={
                'placeholder': 'Salary, Hours, Position, Job Type, '
                               'Address, Job Details and Job Requirements.'
            })
        }
