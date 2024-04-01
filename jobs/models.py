from django.db import models

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
