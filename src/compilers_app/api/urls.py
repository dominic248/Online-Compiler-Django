from django.urls import path, include
from .views import *

urlpatterns = [
    path("python-27/", Python27Compiler.as_view()),
    path("python-38/", Python38Compiler.as_view()),
    path("php-7/", PHP7Compiler.as_view()),
    path("c/", CCompiler.as_view()),
    path("c++/", CPlusPlusCompiler.as_view()),
    path("java-8/", Java8Compiler.as_view()),
    path("java-11/", Java11Compiler.as_view()),
]

