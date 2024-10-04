from rest_framework import serializers
from .models import UploadedFile
from .models import UploadedProjectFile
from .models import VariantRead
from .models import VariantCallProject
from .models import UploadedVariantCallProjectFile
from rest_framework.authtoken.models import Token
from gauth.models import gauthuser

import logging
logger = logging.getLogger(__name__)

# Test Serializers (File Upload)

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ("id", "file", "uploaded_at")


# Variant Read Serializers

class UploadedProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedProjectFile
        fields = ("id", "file", "uploaded_at")

    def create(self, validated_data):
        user_id = Token.objects.get(key=self.context.get("ownerToken")).user_id
        owner = gauthuser.objects.filter(id = user_id)[0]
        project = VariantRead.objects.filter(id = self.context.get("projectID"))[0]
        validated_data["owner"] = owner
        validated_data["project"] = project
        
        return super().create(validated_data)

class VariantReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantRead
        fields = ("id", "name", "genomeURL", "variantURL")

    def create(self, validated_data):
        user_id = Token.objects.get(key=self.context.get("ownerToken")).user_id
        owner = gauthuser.objects.filter(id = user_id)[0]
        validated_data["owner"] = owner
        return super().create(validated_data)

# Variant Call Serializers

class VariantCallProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedVariantCallProjectFile
        fields = ("id", "file", "uploaded_at")

    def create(self, validated_data):
        user_id = Token.objects.get(key=self.context.get("ownerToken")).user_id
        owner = gauthuser.objects.filter(id = user_id)[0]
        project = VariantCallProject.objects.filter(id = self.context.get("callID"))[0]
        validated_data["owner"] = owner
        validated_data["project"] = project

        return super().create(validated_data)

class VariantCallProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantCallProject
        fields = ("id", "name", "referenceGenomeURL", "genomeURL", "vcfURL", "folder", "status")

    def create(self, validated_data):
        user_id = Token.objects.get(key=self.context.get("ownerToken")).user_id
        owner = gauthuser.objects.filter(id = user_id)[0]
        validated_data["owner"] = owner
        return super().create(validated_data)