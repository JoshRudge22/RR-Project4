from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Job, Profile, JobApplication
from django.core import mail

class JobTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.job = Job.objects.create(
            job_title="Software Engineer",
            job_benefits="Health Insurance, 401k",
            address="123 Main St",
            job_details="Develop software solutions",
            job_requirements="2+ years of experience",
            interview_deadline="2024-12-31",
            hired=False
        )

        self.profile = Profile.objects.create(
            user=self.user,
            email="testuser@example.com",
            phone_number="1234567890",
            address="456 Elm St",
            post_code="12345"
        )

        self.client = Client()
        self.client.login(username='testuser', password='testpass')

    def test_jobs_view(self):
        """
        **Expected**: The jobs page should display the job title and use the 'jobs.html' template.
        **Testing**: Make a GET request to the jobs URL and check the response.
        **Result**: Status code 200, 'jobs.html' template used, and job title present in the response.
        """
        response = self.client.get(reverse('jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs.html')
        self.assertContains(response, self.job.job_title)

    def test_profile_view(self):
        """
        **Expected**: The profile page should display the user's profile information and use the 'profile.html' template.
        **Testing**: Make a GET request to the profile URL and check the response.
        **Result**: Status code 200, 'profile.html' template used, and profile email present in the response.
        """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, self.profile.email)

    def test_applying_view(self):
        """
        **Expected**: The applying page should render correctly, and posting valid data should create a JobApplication entry and send an email.
        **Testing**: Make a GET request to the applying URL and a POST request with valid data.
        **Result**: Status code 200 for GET request, status code 302 (redirect) for POST request, JobApplication entry should be created, and an email should be sent.
        """
        response = self.client.get(reverse('applying', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'applying.html')

        response = self.client.post(reverse('applying', args=[self.job.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(JobApplication.objects.filter(user=self.user, job=self.job).exists())
        self.assertEqual(len(mail.outbox), 1)  # Changed from 2 to 1
        self.assertIn(f'You applied to {self.job.job_title}', mail.outbox[0].body)

    def test_delete_profile_view(self):
        """
        **Expected**: The delete profile page should render correctly, and submitting a POST request should delete the profile and associated job applications.
        **Testing**: Make a GET request to the delete profile URL and a POST request.
        **Result**: Status code 200 for GET request, status code 302 (redirect) for POST request, and Profile and associated JobApplications should be deleted.
        """
        response = self.client.get(reverse('delete_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_profile.html')

        response = self.client.post(reverse('delete_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Profile.objects.filter(user=self.user).exists())
        self.assertFalse(JobApplication.objects.filter(user=self.user).exists())

    def test_delete_job_application_view(self):
        """
        **Expected**: Deleting a job application should remove it from the database and redirect to the delete profile page.
        **Testing**: Create a JobApplication entry and make a POST request to delete it.
        **Result**: Status code 302 (redirect) and JobApplication entry should be deleted.
        """
        job_application = JobApplication.objects.create(user=self.user, job=self.job)

        response = self.client.post(reverse('delete_job_application', args=[job_application.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(JobApplication.objects.filter(id=job_application.id).exists())

class JobModelTest(TestCase):
    def test_job_creation(self):
        """
        **Expected**: Creating a Job instance should store the provided data correctly.
        **Testing**: Create a Job instance and verify its attributes.
        **Result**: The attributes of the created Job should match the provided data.
        """
        job = Job.objects.create(
            job_title="Test Job",
            job_benefits="Test Benefits",
            address="Test Address",
            job_details="Test Details",
            job_requirements="Test Requirements",
            interview_deadline="2024-12-31",
            hired=False
        )
        self.assertEqual(job.job_title, 'Test Job')
        self.assertEqual(job.job_benefits, 'Test Benefits')
        self.assertEqual(job.address, 'Test Address')
        self.assertEqual(job.job_details, 'Test Details')
        self.assertEqual(job.job_requirements, 'Test Requirements')
        self.assertEqual(job.interview_deadline, '2024-12-31')
        self.assertFalse(job.hired)

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_profile_creation(self):
        """
        **Expected**: Creating a Profile instance should store the provided data correctly.
        **Testing**: Create a Profile instance and verify its attributes.
        **Result**: The attributes of the created Profile should match the provided data.
        """
        profile = Profile.objects.create(
            user=self.user,
            email="profile@example.com",
            phone_number="0987654321",
            address="789 Oak St",
            post_code="54321"
        )
        self.assertEqual(profile.email, 'profile@example.com')
        self.assertEqual(profile.phone_number, '0987654321')
        self.assertEqual(profile.address, '789 Oak St')
        self.assertEqual(profile.post_code, '54321')

class JobApplicationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.job = Job.objects.create(
            job_title="Test Job",
            job_benefits="Test Benefits",
            address="Test Address",
            job_details="Test Details",
            job_requirements="Test Requirements",
            interview_deadline="2024-12-31",
            hired=False
        )

    def test_job_application_creation(self):
        """
        **Expected**: Creating a JobApplication instance should store the provided data correctly.
        **Testing**: Create a JobApplication instance and verify its attributes.
        **Result**: The attributes of the created JobApplication should match the provided data.
        """
        job_application = JobApplication.objects.create(user=self.user, job=self.job)
        self.assertEqual(job_application.user, self.user)
        self.assertEqual(job_application.job, self.job)