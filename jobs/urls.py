from django.urls import path
from .views import jobs, profile

urlpatterns = [
    path('', jobs, name='jobs'),
    path('profile/', profile, name='profile'),
]