from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.exceptions import TokenBackendError
from rest_framework import exceptions

class CustomAuthMiddleware(authentication.JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None
        
        try:
            validated_token = self.get_validated_token(raw_token)
        except TokenBackendError:
            raise exceptions.AuthenticationFailed()
        
        user = self.get_user(validated_token)
        return user, validated_token