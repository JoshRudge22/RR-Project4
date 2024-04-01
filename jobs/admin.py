from django.contrib import admin
from django import forms 
from .models import Job, AvailableTime

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'address', 'hired')
    list_filter = ('hired',)
    def hired(self, obj):
        return obj.hired
        hired.short_description = 'Filled'
        hired.boolean = True

@admin.register(AvailableTime)
class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ['time']
