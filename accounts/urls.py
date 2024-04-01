from django.urls import path
from .views import home, advertising, contact_view, hiring_form, submitted
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('advertising/', advertising, name='advertising'),
    path('contact/', contact_view, name='contact'),
    path('hiring/', hiring_form, name='hiring'),
    path('submitted/', submitted, name='submitted'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]