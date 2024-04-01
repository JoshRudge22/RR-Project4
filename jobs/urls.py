from django.urls import path
from .views import jobs, profile, submitted

urlpatterns = [
    path('', jobs, name='jobs'),
    path('profile/', profile, name='profile'),
    path('submitted/', submitted, name='submitted'),
]