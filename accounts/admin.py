from django.contrib import admin
from .models import ContactUsForm, Hiring

admin.site.register(ContactUsForm)


class HiringAdmin(admin.ModelAdmin):
    list_display = [
        'company_name', 'email', 'phone_number',
        'job_description', 'download_job_doc'
    ]

    def download_job_doc(self, obj):
        if obj.documentation:
            return '<a href="{0}">Download</a>'.format(obj.job_doc.url)
        else:
            return "No document attached"
    download_job_doc.allow_tags = True
    download_job_doc.short_description = 'Job Document'


admin.site.register(Hiring, HiringAdmin)
