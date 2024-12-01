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
from .views import updateCallLinks
from .views import fetchCalls
from .views import fetchCall
from .views import deleteCall
from .views import runCall
from .views import fetchAllReads
from .views import fetchAllCalls
from .views import fetchAllUsers

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
    path('updatecalllinks/', updateCallLinks, name='update-call-links' ),

    path('fetchcalls/', fetchCalls, name="fetch-calls"),
    path('fetchcall/', fetchCall, name="fetch-call"),
    path('deletecall/', deleteCall, name="delete-call"),
    path('runcall/', runCall, name="run-call"),
    
    path('fetchAllReads/', fetchAllReads, name="all-reads"),
    path('fetchAllCalls/', fetchAllCalls, name="all-calls"),
    path('fetchAllUsers/', fetchAllUsers, name="all-users"),
]