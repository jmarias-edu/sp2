from django.urls import path
from .views import upload_file
from .views import create_project

urlpatterns = [
    path('upload/', upload_file, name='upload-file'),
    path('createproject/', create_project, name='create-project')
]