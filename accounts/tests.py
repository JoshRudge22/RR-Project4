from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from .models import ContactUsForm, Hiring
from .forms import ContactForm, HiringForm
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')
        self.valid_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'phone_number': '1234567890',
            'message': 'This is a test message.',
            'best_time_to_contact': 'morning'
        }

    def test_contact_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post_valid(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('submitted_contact'))
        self.assertEqual(ContactUsForm.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('New Contact Form Submission', mail.outbox[0].subject)

    def test_contact_view_post_invalid(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'invalid-email'
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

class HiringFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('hiring')
        self.valid_data = {
            'company_name': 'Test Company',
            'email': 'testcompany@example.com',
            'phone_number': '1234567890',
            'job_description': 'This is a test job description.',
        }
        self.valid_file = SimpleUploadedFile("test.txt", b"file_content")

    def test_hiring_form_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hiring.html')

    def test_hiring_form_post_valid(self):
        data = self.valid_data.copy()
        data['documentation'] = self.valid_file
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('submitted_hiring'))
        self.assertEqual(Hiring.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('New Hiring Form Submission', mail.outbox[0].subject)

    def test_hiring_form_post_invalid(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'invalid-email'
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hiring.html')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

class ContactUsFormModelTest(TestCase):
    def test_contact_us_form_creation(self):
        form = ContactUsForm.objects.create(
            name='Test User',
            email='testuser@example.com',
            phone_number='1234567890',
            message='This is a test message.',
            best_time_to_contact='morning'
        )
        self.assertEqual(form.name, 'Test User')
        self.assertEqual(form.email, 'testuser@example.com')
        self.assertEqual(form.phone_number, '1234567890')
        self.assertEqual(form.message, 'This is a test message.')
        self.assertEqual(form.best_time_to_contact, 'morning')

class HiringModelTest(TestCase):
    def test_hiring_creation(self):
        hiring = Hiring.objects.create(
            company_name='Test Company',
            email='testcompany@example.com',
            phone_number='1234567890',
            job_description='This is a test job description.',
            documentation=SimpleUploadedFile("test.txt", b"file_content")
        )
        self.assertEqual(hiring.company_name, 'Test Company')
        self.assertEqual(hiring.email, 'testcompany@example.com')
        self.assertEqual(hiring.phone_number, '1234567890')
        self.assertEqual(hiring.job_description, 'This is a test job description.')
        self.assertTrue(hiring.documentation.name.endswith('test.txt'))

class ContactFormTest(TestCase):
    def test_contact_form_valid(self):
        form_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'phone_number': '1234567890',
            'message': 'This is a test message.',
            'best_time_to_contact': 'morning'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        form_data = {
            'name': 'Test User',
            'email': 'invalid-email',
            'phone_number': '1234567890',
            'message': 'This is a test message.',
            'best_time_to_contact': 'morning'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

class HiringFormTest(TestCase):
    def test_hiring_form_valid(self):
        form_data = {
            'company_name': 'Test Company',
            'email': 'testcompany@example.com',
            'phone_number': '1234567890',
            'job_description': 'This is a test job description.'
        }
        form = HiringForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_hiring_form_invalid(self):
        form_data = {
            'company_name': 'Test Company',
            'email': 'invalid-email',
            'phone_number': '1234567890',
            'job_description': 'This is a test job description.'
        }
        form = HiringForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])