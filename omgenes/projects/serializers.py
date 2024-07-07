from rest_framework import serializers
from .models import UploadedFile
from .models import VariantRead
from rest_framework.authtoken.models import Token
from gauth.models import gauthuser



import logging
logger = logging.getLogger(__name__)

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ("id", "file", "uploaded_at")


class VariantReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantRead
        fields = ("id", "name", "genomeURL", "variantURL")

    def create(self, validated_data):

        user_id = Token.objects.get(key=self.context.get("ownerToken")).user_id
        owner = gauthuser.objects.filter(id = user_id)[0]
        validated_data["owner"] = owner
        return super().create(validated_data)