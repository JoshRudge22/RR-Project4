from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]