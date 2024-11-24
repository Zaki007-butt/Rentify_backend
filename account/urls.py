#Django Imports
from django.urls import path

#Local Imprts
from account.views import (
  UserRegistrationView,
  UserLoginView,
  UserProfileView,
  UserChangePasswordView,
  UserUpdateView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
  path('register', UserRegistrationView.as_view()),
  path('login', UserLoginView.as_view()),
  path('profile', UserProfileView.as_view()),
  path('refresh', TokenRefreshView.as_view()),
  path('change-password', UserChangePasswordView.as_view()),
  path('update-profile', UserUpdateView.as_view()),
]
