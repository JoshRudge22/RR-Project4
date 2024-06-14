from django.urls import path
from .views import jobs, profile, applying, submitted_applying, delete_profile, delete_job_application

urlpatterns = [
    path('', jobs, name='jobs'),
    path('profile/', profile, name='profile'),
    path('applying/<int:job_id>/', applying, name='applying'),
    path('submitted_applying/', submitted_applying, name='submitted_applying'),
    path('delete_profile/', delete_profile, name='delete_profile'),
     path('delete_job_application/<int:job_id>/', delete_job_application, name='delete_job_application'),
]
