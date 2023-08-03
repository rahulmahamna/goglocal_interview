from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import authentication

class CustomMiddleware(authentication.BaseAuthentication):
    def authenticate(self, request):
        if request.headers['Authorization']:
            access_token = AccessToken(request.headers['Authorization'])
            user = User.objects.get(id=access_token['user_id'])
            request.user = user
        return request
        # return super().authenticate(request)