from django.shortcuts import render


# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from .serializers import VariantReadSerializer

import logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_project(request):
    if request.method == 'POST':

        serializer = VariantReadSerializer(data=request.data, context={"ownerToken": request.POST.get("token").split(" ")[1]})

        serializer.is_valid()
        logger.info(f"Serializer Error: {serializer.errors}")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)