from rest_framework import serializers
from new_app.models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    
    class Meta:
        model = User