from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Job, Profile, JobApplication

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
        response = self.client.get(reverse('jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs.html')
        self.assertContains(response, self.job.job_title)

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, self.profile.email)

    def test_applying_view(self):
        response = self.client.get(reverse('applying', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'applying.html')

        response = self.client.post(reverse('applying', args=[self.job.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(JobApplication.objects.filter(user=self.user, job=self.job).exists())

    def test_delete_profile_view(self):
        response = self.client.get(reverse('delete_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_profile.html')

        response = self.client.post(reverse('delete_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Profile.objects.filter(user=self.user).exists())

    def test_delete_job_application_view(self):
        job_application = JobApplication.objects.create(user=self.user, job=self.job)

        response = self.client.post(reverse('delete_job_application', args=[job_application.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(JobApplication.objects.filter(id=job_application.id).exists())