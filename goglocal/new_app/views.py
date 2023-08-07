from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from new_app.serializers import LoginSerializer, ProfileSerializer
from new_app.models import User
# from django.contrib.auth.models import User
from new_app.utils import SerializerResponses, get_login_user_data
from django.contrib.auth import authenticate

# Create your views here.

class Login(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request):
        validate_serializer = self.serializer_class(data=request.data)
        if not validate_serializer.is_valid():
            return SerializerResponses().call(validate_serializer.errors)

        user = authenticate(**request.data)
        if user:
            return Response(get_login_user_data(user))
        

class Profile(RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).first()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset())
        return Response(data=serializer.data, status=HTTP_200_OK)