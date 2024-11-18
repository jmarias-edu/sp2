from django.urls import path
from .views import verify_google_token
from .views import get_user_data
from .views import checkIfAdmin
from .views import deleteUser
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('verify-google-token/', verify_google_token, name='verify_google_token'),
    path('fetch-user/', get_user_data, name='get_user'),
    path('check-admin/', checkIfAdmin, name='check-admin'),
    path('delete-user/', deleteUser, name='delete-user')
]