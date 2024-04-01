from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_benefits = models.TextField()
    address = models.CharField(max_length=60)
    job_details = models.TextField()    
    job_requirements = models.TextField()
    interview_deadline = models.DateField(blank=True, null=True)
    available_times = models.ManyToManyField('AvailableTime', related_name='jobs')
    hired = models.BooleanField()
    notes = models.TextField(null=True)

    def __str__(self):
        return self.job_title

class AvailableTime(models.Model):
    TIME_CHOICES = [
        ('10:00 - 11:00', '10:00 - 11:00'),
        ('11:00 - 12:00', '11:00 - 12:00'),
        ('12:00 - 13:00', '12:00 - 13:00'),
        ('13:00 - 14:00', '13:00 - 14:00'),
        ('14:00 - 15:00', '14:00 - 15:00'),
        ('15:00 - 16:00', '15:00 - 16:00'),
    ]
    time = models.CharField(max_length=20, choices=TIME_CHOICES)

    def __str__(self):
        return self.time

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    cv = models.FileField(upload_to='cv/', blank=True)
    address = models.CharField(max_length=100, blank=True)
    notice = models.ManyToManyField('NoticeTimes')

    def __str__(self):
        return self.user.username


class NoticeTimes(models.Model):
    NOTICE_CHOICES = [
        ('ASAP', 'ASAP'),
        ('1 Week', '1 Week'),
        ('2 Weeks', '2 Weeks'),
        ('3 Weeks', '3 Weeks'),
        ('4 Week or more', '4 Weeks or more'),
    ]
    notice = models.CharField(max_length=20, choices=NOTICE_CHOICES)

    def __str__(self):
        return self.notice

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    
    def __str__(self):
        return f"Application for {self.job} by {self.user.username}"