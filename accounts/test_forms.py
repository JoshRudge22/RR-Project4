from django.test import TestCase
from .models import ContactUsForm, Hiring

class ContactUsFormTest(TestCase):
    def test_contact_form_creation(self):
        contact_form = ContactUsForm.objects.create(
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            message='This is a test message.',
            best_time_to_contact='morning'
        )

class HiringTest(TestCase):
    def test_hiring_creation(self):
        hiring = Hiring.objects.create(
            company_name='ABC Inc.',
            email='hr@abc.com',
            phone_number='9876543210',
            job_description='Software Engineer position',
            documentation=None
        )
