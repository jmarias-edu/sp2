from rest_framework import serializers
from .models import gauthuser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = gauthuser
        fields = ['f_name', 'l_name', 'email']