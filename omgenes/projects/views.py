from django.shortcuts import render


# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import UploadedFile
from .models import VariantRead
from .serializers import UploadedFileSerializer
from .serializers import UploadedProjectFileSerializer
from .serializers import VariantReadSerializer
from .serializers import VariantCallProjectSerializer
from .serializers import VariantCallProjectFileSerializer
from django.http import JsonResponse
from gauth.models import gauthuser

import logging
logger = logging.getLogger(__name__)

# Upload File Test View

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Variant Read Views

# Create Project Function
@api_view(['POST'])
def create_project(request):
    if request.method == 'POST':

        serializer = VariantReadSerializer(data=request.data, context={"ownerToken": request.POST.get("token").split(" ")[1]})

        # serializer.is_valid()
        # logger.info(f"Serializer Error: {serializer.errors}")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Project links Function
@api_view(['PATCH'])
def updateProjectLinks(request):
    read = VariantRead.objects.filter(id=request.data["readID"])[0]
    serializer = VariantReadSerializer(read, data={"genomeURL":request.data["genome"], "variantURL": request.data["vcf"]}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Fetch project reads
@api_view(['POST'])
def fetchReads(request):
    if request.method == 'POST':
        token = request.POST.get("token").split(" ")[1]

        user_id = Token.objects.get(key=token).user_id
        owner = gauthuser.objects.filter(id = user_id)[0]

        reads = VariantRead.objects.filter(owner=owner)

        serializer = VariantReadSerializer(reads, many=True)
        return JsonResponse({"reads": serializer.data}, status=200)

# Fetch Project Details
@api_view(['POST'])
def fetchRead(request):
    if request.method == 'POST':
        token = request.POST.get("token").split(" ")[1]
        read_id = request.POST.get("readid")

        user_id = Token.objects.get(key=token).user_id
        owner = gauthuser.objects.filter(id = user_id)[0]

        reads = VariantRead.objects.filter(owner=owner, id=read_id)[0]

        serializer = VariantReadSerializer(reads)
        logger.info(serializer.data)
        return JsonResponse({"reads": serializer.data}, status=200)

# Delete Project Read
@api_view(["POST"])
def deleteRead(request):
    if request.method == "POST":
        logger.info(request.POST.get("readid"))
        read_id = request.POST.get("readid")
        read = VariantRead.objects.filter(id=read_id)[0]
        read.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Variant Call Views

# Create Variant Call project
@api_view(["POST"])
def createVariantCall(request):
    if request.method == "POST":
        serializer = VariantCallProjectSerializer(data=request.data, context={"ownerToken": request.POST.get("token").split(" ")[1]})
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"reads": serializer.data}, status=200)
        return JsonResponse({"reads": serializer.error}, status=400)

# Upload Variant Call File
@api_view(['POST'])
def upload_project_file(request):
    if request.method == 'POST':
        serializer = UploadedProjectFileSerializer(data=request.data, context={"ownerToken":request.POST.get("token").split(" ")[1], "callID": request.POST.get("callid")})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Project Links

# Delete Variant Call