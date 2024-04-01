from django.urls import path
from .views import jobs, profile, applying, submitted

urlpatterns = [
    path('', jobs, name='jobs'),
    path('profile/', profile, name='profile'),
    path('applying/<int:job_id>/', applying, name='applying'),
    path('submitted/', submitted, name='submitted'),
]