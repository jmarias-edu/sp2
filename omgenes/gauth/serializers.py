from rest_framework import serializers
from .models import gauthuser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = gauthuser
        fields = ['id', 'f_name', 'l_name', 'email', "user_id"]