from django.urls import path
from .views import home, contact_view, hiring_form, submitted
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('hiring/', hiring_form, name='hiring'),
    path('submitted/', submitted, name='submitted'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]