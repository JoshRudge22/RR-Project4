from django.urls import path
from .views import jobs

urlpatterns = [
    path('', jobs, name='jobs'),
]