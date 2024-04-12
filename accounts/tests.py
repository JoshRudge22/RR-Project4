from django.test import TestCase
from .forms import ContactForm, HiringForm


class TestForms(TestCase):
    def test_contact_form_empty_inputs(self):
        """Test if contact form is invalid with empty inputs"""
        form_data = {
            'name': '',
            'email': '',
            'phone_number': '',
            'message': '',
            'best_time_to_contact': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_hiring_form_empty_inputs(self):
        """Test if hiring form is invalid with empty inputs"""
        form_data = {
            'name': '',
            'email': '',
            'resume': ''
        }
        form = HiringForm(data=form_data)
        self.assertFalse(form.is_valid())
