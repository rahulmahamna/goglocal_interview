from rest_framework import serializers
from new_app.models import User
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            user = User.objects.filter(username=attrs['username']).first()
            if not user:
                raise serializers.ValidationError('Please enter valid password')
        if not user.is_approved:
            raise serializers.ValidationError('Please wait until your account has been approved by Admin')
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
        )