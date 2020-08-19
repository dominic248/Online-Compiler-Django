from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

# For listing all users and creating new user, to view a single user append '/1' that is '/id' in the URL  path 'list/fullinfo'
router.register(r"", UsersFullInfoAPIView)

urlpatterns = [
    path("create/", UsersCreateInfoAPIView.as_view()),
    path("", include(router.urls)),
    # path("user/currentuser/", CurrentUserAPIView.as_view()),
]

