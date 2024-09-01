from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import ContactUsForm, Hiring
from .forms import ContactForm, HiringForm

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

    def test_contact_form_page_elements(self):
        """
        **Expected**: The contact form page should include the name, email, phone number, message, and best time to contact fields, as well as a submit button.
        **Testing**: Make a GET request to the contact URL and check for the presence of each form element.
        **Result**: The fields 'name', 'email', 'phone_number', 'message', 'best_time_to_contact', and the submit button should be present in the HTML.
        """
        response = self.client.get(self.url)
        self.assertContains(response, '<input type="text" name="name"')
        self.assertContains(response, '<input type="email" name="email"')
        self.assertContains(response, '<input type="text" name="phone_number"')
        self.assertContains(response, '<textarea name="message"')
        self.assertContains(response, '<select name="best_time_to_contact"')
        self.assertContains(response, '<button type="submit"')

    def test_contact_form_post_valid(self):
        """
        **Expected**: Submitting valid data should redirect to 'submitted_contact', create a ContactUsForm entry, and send an email.
        **Testing**: POST valid data to the contact form URL.
        **Result**: Status code 302 (redirect), 'submitted_contact' URL, one ContactUsForm entry in the database, and one email sent.
        """
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('submitted_contact'))
        self.assertEqual(ContactUsForm.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('New Contact Form Submission', mail.outbox[0].subject)

    def test_contact_form_post_invalid_email(self):
        """
        **Expected**: Submitting data with an invalid email should show an error message and keep the user on the contact page.
        **Testing**: POST data with an invalid email to the contact form URL.
        **Result**: Status code 200, 'contact.html' template, and form error on the email field.
        """
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'invalid-email'
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_contact_form_post_empty_fields(self):
        """
        **Expected**: Submitting an empty form should show errors for all required fields and keep the user on the contact page.
        **Testing**: POST empty data to the contact form URL.
        **Result**: Status code 200, 'contact.html' template, and form errors for required fields.
        """
        empty_data = {}
        response = self.client.post(self.url, empty_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')

    def test_contact_form_post_long_input(self):
        """
        **Expected**: Submitting data with too long input should show an error message.
        **Testing**: POST data with long input to the contact form URL.
        **Result**: Status code 200, 'contact.html' template, and form error on the name field.
        """
        long_data = self.valid_data.copy()
        long_data['name'] = 'a' * 101
        response = self.client.post(self.url, long_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFormError(response, 'form', 'name', 'Ensure this value has at most 100 characters (it has 101).')

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

    def test_contact_view_post_empty_fields(self):
        empty_data = {}
        response = self.client.post(self.url, empty_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')

    def test_contact_view_post_long_input(self):
        long_data = self.valid_data.copy()
        long_data['name'] = 'a' * 101
        response = self.client.post(self.url, long_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFormError(response, 'form', 'name', 'Ensure this value has at most 100 characters (it has 101).')

    def test_contact_view_post_valid_with_message(self):
        response = self.client.post(self.url, self.valid_data, follow=True)
        self.assertRedirects(response, reverse('submitted_contact'))
        self.assertEqual(ContactUsForm.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('New Contact Form Submission', mail.outbox[0].subject)

    def test_contact_view_post_invalid_does_not_create_entry(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'invalid-email'
        initial_count = ContactUsForm.objects.count()
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(ContactUsForm.objects.count(), initial_count)


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
        self.valid_file = SimpleUploadedFile("test.txt", b"file_content", content_type="text/plain")

    def test_hiring_form_page_elements(self):
        """
        **Expected**: The hiring form page should include the company name, email, phone number, job description fields, and a file upload input, as well as a submit button.
        **Testing**: Make a GET request to the hiring URL and check for the presence of each form element.
        **Result**: The fields 'company_name', 'email', 'phone_number', 'job_description', and the file upload input, and the submit button should be present in the HTML.
        """
        response = self.client.get(self.url)
        self.assertContains(response, '<input type="text" name="company_name"')
        self.assertContains(response, '<input type="email" name="email"')
        self.assertContains(response, '<input type="text" name="phone_number"')
        self.assertContains(response, '<textarea name="job_description"')
        self.assertContains(response, '<input type="file" name="documentation"')
        self.assertContains(response, '<button type="submit"')

    def test_hiring_form_post_valid(self):
        """
        **Expected**: Submitting valid data including a file should redirect to 'submitted_hiring', create a Hiring entry, and send an email.
        **Testing**: POST valid data with a file to the hiring URL.
        **Result**: Status code 302 (redirect), 'submitted_hiring' URL, one Hiring instance in the database, and one email sent.
        """
        data = self.valid_data.copy()
        data['documentation'] = self.valid_file
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('submitted_hiring'))
        self.assertEqual(Hiring.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('New Hiring Form Submission', mail.outbox[0].subject)

    def test_hiring_form_post_empty_fields(self):
        """
        **Expected**: Submitting empty data should show errors for all required fields and keep the user on the hiring page.
        **Testing**: POST empty data to the hiring form URL.
        **Result**: Status code 200, 'hiring.html' template, and form errors for required fields.
        """
        empty_data = {}
        response = self.client.post(self.url, empty_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hiring.html')
        self.assertFormError(response, 'form', 'company_name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'phone_number', 'This field is required.')
        self.assertFormError(response, 'form', 'job_description', 'This field is required.')
        self.assertFormError(response, 'form', 'documentation', 'This field is required.')

    def test_hiring_form_post_invalid_file_type(self):
        """
        **Expected**: Submitting a file of invalid type should show an error message and keep the user on the hiring page.
        **Testing**: POST invalid file type data to the hiring form URL.
        **Result**: Status code 200, 'hiring.html' template, and form error on file type.
        """
        invalid_file = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        data = self.valid_data.copy()
        data['documentation'] = invalid_file
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hiring.html')
        self.assertFormError(response, 'form', 'documentation', 'Upload a valid file. The file type is not supported.')

    def test_hiring_form_post_valid_with_message(self):
        """
        **Expected**: Submitting valid data with a file should send an email notification.
        **Testing**: POST valid data with a file to the hiring URL.
        **Result**: One email sent with the subject 'New Hiring Form Submission'.
        """
        data = self.valid_data.copy()
        data['documentation'] = self.valid_file
        response = self.client.post(self.url, data, follow=True)
        self.assertRedirects(response, reverse('submitted_hiring'))
        self.assertEqual(Hiring.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('New Hiring Form Submission', mail.outbox[0].subject)

    def test_hiring_form_post_invalid_does_not_create_entry(self):
        invalid_file = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        invalid_data = self.valid_data.copy()
        invalid_data['documentation'] = invalid_file
        initial_count = Hiring.objects.count()
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(Hiring.objects.count(), initial_count)

class ContactUsFormModelTest(TestCase):
    def test_contact_us_form_creation(self):
        """
        **Expected**: Creating a ContactUsForm instance should store the provided data correctly.
        **Testing**: Create a ContactUsForm instance and verify its attributes.
        **Result**: The attributes of the created ContactUsForm should match the provided data.
        """
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
        """
        **Expected**: Creating a Hiring instance with a file should store the provided data and the file correctly.
        **Testing**: Create a Hiring instance with a file and verify its attributes.
        **Result**: The attributes of the created Hiring instance should match the provided data, and the file should be saved.
        """
        file = SimpleUploadedFile("test.txt", b"file_content", content_type="text/plain")
        hiring = Hiring.objects.create(
            company_name='Test Company',
            email='testcompany@example.com',
            phone_number='1234567890',
            job_description='This is a test job description.',
            documentation=file
        )
        self.assertEqual(hiring.company_name, 'Test Company')
        self.assertEqual(hiring.email, 'testcompany@example.com')
        self.assertEqual(hiring.phone_number, '1234567890')
        self.assertEqual(hiring.job_description, 'This is a test job description.')
        self.assertTrue(hiring.documentation.name.endswith('.txt'))

class ContactFormTest(TestCase):
    def test_contact_form_valid(self):
        """
        **Expected**: The contact form should be valid with correct data.
        **Testing**: Validate the form with correct data.
        **Result**: The form should be valid.
        """
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
        """
        **Expected**: The contact form should be invalid with incorrect email data.
        **Testing**: Validate the form with incorrect email data.
        **Result**: The form should be invalid, and the email field should have an error.
        """
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
        """
        **Expected**: The hiring form should be valid with correct data.
        **Testing**: Validate the form with correct data.
        **Result**: The form should be valid.
        """
        form_data = {
            'company_name': 'Test Company',
            'email': 'testcompany@example.com',
            'phone_number': '1234567890',
            'job_description': 'This is a test job description.'
        }
        form = HiringForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_hiring_form_invalid(self):
        """
        **Expected**: The hiring form should be invalid with incorrect email data.
        **Testing**: Validate the form with incorrect email data.
        **Result**: The form should be invalid, and the email field should have an error.
        """
        form_data = {
            'company_name': 'Test Company',
            'email': 'invalid-email',
            'phone_number': '1234567890',
            'job_description': 'This is a test job description.'
        }
        form = HiringForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])