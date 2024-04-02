from django.urls import path
from .views import jobs, profile, applying, submitted_applying

urlpatterns = [
    path('', jobs, name='jobs'),
    path('profile/', profile, name='profile'),
    path('applying/<int:job_id>/', applying, name='applying'),
    path('submitted_applying/', submitted_applying, name='submitted_applying'),
]