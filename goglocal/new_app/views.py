from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from new_app.serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# from new_app.models import User
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.

class Login(APIView):
    # serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request):
        # serialiser = self.serializer_class(data=request.data)
        # if not serialiser.is_valid():
        #     return Response(data=serialiser.error_messages, status=HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=request.data['username']).first()
        if not user:
            return Response(status=HTTP_400_BAD_REQUEST, data={"message": "Invalid request"})
        if not check_password(request.data['password'], user.password):
            return Response(status=HTTP_400_BAD_REQUEST, data={"message": "Invalid request"})
        refresh = RefreshToken.for_user(user)
        return Response(data={"token":str(refresh.access_token)},status=HTTP_200_OK)
        

class Profile(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        return Response()