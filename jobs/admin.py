from django.contrib import admin
from django import forms
from .models import Job, AvailableTime, NoticeTimes, JobApplication
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    list_display = ('job_title', 'address', 'hired')
    list_filter = ('hired',)

    def hired(self, obj):
        return obj.hired
        hired.short_description = 'Filled'
        hired.boolean = True


@admin.register(AvailableTime)
class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ['time']


@admin.register(NoticeTimes)
class NoticeTimesAdmin(admin.ModelAdmin):
    list_display = ['notice']


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['user']
