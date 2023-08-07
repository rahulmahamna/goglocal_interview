from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class SerializerResponses:

    def get_error_messsage(self, errors):

        for key,value in errors.items():
            if key == 'non_field_errors':
                return value[0]
            return f"{key}: {value[0]}"

    def call(self, serializer_errors, status=status.HTTP_400_BAD_REQUEST):
        message = self.get_error_messsage(serializer_errors)
        return Response(
                {
                    "message": message,
                    "status": False
                },
                status = status
            )

def get_login_user_data(user):
    payload = RefreshToken.for_user(user).access_token
    return str(payload)