from django.urls import path
from .views import upload_file
from .views import create_project
from .views import fetchReads
from .views import fetchRead
from .views import upload_project_file
from .views import updateProjectLinks
from .views import deleteRead
from .views import createVariantCall
from .views import uploadCallFile

urlpatterns = [
    path('upload/', upload_file, name='upload-file'),
    path('uploadfile/', upload_project_file, name='upload-project-file'),

    path('createproject/', create_project, name='create-project'),
    path('updateprojlinks/', updateProjectLinks, name='update-project-links'),
    path("deleteproject/", deleteRead, name='delete-project'),

    path('fetchreads/', fetchReads, name='fetch-reads'),
    path('fetchread/', fetchRead, name='fetch-read'),

    path('uploadcallfile/', uploadCallFile, name='upload-call-file'),
    path('createcall/', createVariantCall, name='create-call'),
    # path('updatecalllinks/'),
    # path('deletecall/'),

    # path('fetchcalls/'),
    # path('fetchcall/'),
]