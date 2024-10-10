from django.shortcuts import render
import json
import os
import subprocess

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import UploadedFile
from .models import VariantRead
from .models import VariantCallProject
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

@api_view(['POST'])
def upload_project_file(request):
    if request.method == 'POST':
        serializer = UploadedProjectFileSerializer(data=request.data, context={"ownerToken":request.POST.get("token").split(" ")[1], "projectID": request.POST.get("projid")})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Project links Function
@api_view(['PATCH'])
def updateProjectLinks(request):
    try:
        read = VariantRead.objects.filter(id=request.data["readID"])[0]
        serializer = VariantReadSerializer(read, data={"genomeURL":request.data["genome"], "variantURL": request.data["vcf"]}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)

# Fetch project reads
@api_view(['POST'])
def fetchReads(request):
    if request.method == 'POST':
        try:
            token = request.POST.get("token").split(" ")[1]

            user_id = Token.objects.get(key=token).user_id
            owner = gauthuser.objects.filter(id = user_id)[0]

            reads = VariantRead.objects.filter(owner=owner)

            serializer = VariantReadSerializer(reads, many=True)
            return JsonResponse({"reads": serializer.data}, status=200)

        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)

# Fetch Project Details
@api_view(['POST'])
def fetchRead(request):
    if request.method == 'POST':
        try:
            token = request.POST.get("token").split(" ")[1]
            read_id = request.POST.get("readid")

            user_id = Token.objects.get(key=token).user_id
            owner = gauthuser.objects.filter(id = user_id)[0]

            reads = VariantRead.objects.filter(owner=owner, id=read_id)[0]

            serializer = VariantReadSerializer(reads)
            # logger.info(serializer.data)
            return JsonResponse({"reads": serializer.data}, status=200)
        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)


# Delete Project Read
@api_view(["POST"])
def deleteRead(request):
    if request.method == "POST":
        try:
            # logger.info(request.POST.get("readid"))
            read_id = request.POST.get("readid")
            read = VariantRead.objects.filter(id=read_id)[0]
            read.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)

# Variant Call Views

# Create Variant Call project
@api_view(["POST"])
def createVariantCall(request):
    if request.method == "POST":
        serializer = VariantCallProjectSerializer(data=request.data, context={"ownerToken": request.POST.get("token").split(" ")[1]})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Upload Variant Call File
@api_view(["POST"])
def uploadCallFile(request):
    if request.method == "POST":
        serializer = VariantCallProjectFileSerializer(data=request.data, context={"ownerToken": request.POST.get("token").split(" ")[1], "callID": request.POST.get("callid")})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Project Links
@api_view(['PATCH'])
def updateCallLinks(request):
    try:
        read = VariantCallProject.objects.filter(id=request.data["callid"])[0]
        serializer = VariantCallProjectSerializer(read, data={"genomeURL":request.data["genome"], "referenceGenomeURL": request.data["ref"]}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)


# Fetch Variant Calls
@api_view(['POST'])
def fetchCalls(request):
    if request.method == 'POST':
        try:
            token = request.POST.get("token").split(" ")[1]
            user_id = Token.objects.get(key=token).user_id

            owner = gauthuser.objects.filter(id = user_id)[0]
            reads = VariantCallProject.objects.filter(owner=owner)
            serializer = VariantCallProjectSerializer(reads, many=True)
            return JsonResponse({"calls": serializer.data}, status=200)
        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)


# Fetch Call Details
@api_view(['POST'])
def fetchCall(request):
    if request.method == 'POST':
        try:
            token = request.POST.get("token").split(" ")[1]
            call_id = request.POST.get("callid")

            user_id = Token.objects.get(key=token).user_id
            owner = gauthuser.objects.filter(id = user_id)[0]

            reads = VariantCallProject.objects.filter(owner=owner, id=call_id)[0]
            
            serializer = VariantCallProjectSerializer(reads)

            # logger.info(serializer.data)
            
            return JsonResponse({"calls": serializer.data}, status=200)
        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)


# Delete Variant Call
@api_view(["POST"])
def deleteCall(request):
    if request.method == "POST":
        try:
            # logger.info(request.POST.get("callid"))
            read_id = request.POST.get("callid")
            read = VariantCallProject.objects.filter(id=read_id)[0]
            read.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)

def runVariantCall(variantCall):
    ref = "./omgenes" + variantCall.referenceGenomeURL
    ref = ref.replace("http://localhost:8000", "")
    target = "./omgenes" + variantCall.genomeURL
    target = target.replace("http://localhost:8000", "")
    folder = "./omgenes/media/" + variantCall.folder[:-1]

    print(ref)
    print(target)
    print(folder)

    snakemake_cmd = [
        "conda", "run", "-n", "snakemake",  # Replace with your Snakemake environment name
        "snakemake", 
        "--snakefile", "./workflows/snakefile",
        "--cores", "1",  # Adjust cores as needed
        "--config",
        f"ref={ref}", 
        f"target={target}",
        f"folder={folder}",
        "--forceall", "-p"
    ]

    # logger.info(f"Call Status: {variantCall}")
    

    #Add changing of the vcf kinemerlu uwu
    try:
        # Run the variant call using Snakemake
        result = subprocess.run(snakemake_cmd, check=True, capture_output=True)
        variantCall.status = "Completed"
        vcfFile = target.replace("./omgenes/media/", "")
        variantCall.vcfURL = f"http://localhost:8000/media/{vcfFile}.vcf"
        # print(result.stdout)
        log = result.stderr.decode("utf-8", "strict").split("\n")[-3].split(" ")[2]
        copy = subprocess.run(["cp", log, folder])
        variantCall.log = f"http://localhost:8000/media/{folder.replace("./omgenes/media/","")}/{log.replace(".snakemake/log/","")}"
    except subprocess.CalledProcessError as e:
        # Log error and mark the job as failed
        variantCall.status = "Failed"
        print(f"Error: {e}")
    finally:
        variantCall.save()

    return variantCall.status

# Run Variant Calls
@api_view(["POST"])
def runCall(request):
    if request.method == 'POST':
        try:
            token = request.POST.get("token").split(" ")[1]
            call_id = request.POST.get("callid")

            user_id = Token.objects.get(key=token).user_id
            owner = gauthuser.objects.filter(id = user_id)[0]

            call = VariantCallProject.objects.filter(owner=owner, id=call_id)[0]

            runVariantCall(call)

            return JsonResponse({"Test": True}, status=200)
            
        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def checkCall(request):
    pass
