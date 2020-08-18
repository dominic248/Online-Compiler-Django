from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
import jwt
from django.conf import settings
import time


class MyBackend(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None
        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None
        validated_token = self.get_validated_token(raw_token)
        # print(validated_token)
        user = self.get_user(validated_token)
        # print("token: ",user,type(user))
        return user, None

    def get_validated_token(self, raw_token):
        messages = []
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                auth_token = AuthToken(raw_token)
                token = raw_token.decode("utf-8")
                decoded_token = jwt.decode(
                    token, settings.SECRET_KEY, algorithms=["HS256"]
                )
                all_logout_date = (
                    int(self.get_user(auth_token).all_logout.strip() or 0)
                    if self.get_user(auth_token).all_logout
                    else 0
                )
                if (
                    all_logout_date > int(decoded_token["issued"])
                    and all_logout_date != 0
                ):
                    messages.append(
                        {
                            "token_class": AuthToken.__name__,
                            "token_type": AuthToken.token_type,
                            "message": "Token has Expired!!!",
                        }
                    )
                else:
                    return auth_token
            except TokenError as e:
                messages.append(
                    {
                        "token_class": AuthToken.__name__,
                        "token_type": AuthToken.token_type,
                        "message": e.args[0],
                    }
                )
        raise InvalidToken(
            {
                "detail": ("Given token not valid for any token type"),
                "messages": messages,
            }
        )
