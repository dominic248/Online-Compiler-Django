import jwt, json
from rest_framework import views, status, exceptions, serializers
from rest_framework.response import Response
from django.http import HttpResponse
from django.conf import settings
from rest_framework.authentication import get_authorization_header, BaseAuthentication

from django.contrib.auth import get_user_model

Users = get_user_model()

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import time
from datetime import datetime


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(user)
        # Add custom claims
        token["name"] = user.username
        token["issued"] = int(time.time())
        # ts = int("1590133318")
        # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        # print(time.strftime("%D %H:%M", time.localtime(ts)))
        return token

    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        print(data)
        data.update({"username": self.user.username})
        data.update({"id": self.user.id})
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
