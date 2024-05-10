from django.urls import path
from .views import verify_google_token

urlpatterns = [
    path('verify-google-token/', verify_google_token, name='verify_google_token'),
]