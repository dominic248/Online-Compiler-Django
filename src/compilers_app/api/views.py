# import subprocess
# run=subprocess.Popen(["python3.8", "run.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# grep_stdout =run.communicate(input=b'one\ntwo\nthree\nfour\n')[0]
# print(grep_stdout.decode())
# print(run.returncode)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated
import os
import subprocess
import json
from codecs import encode


class Python27Compiler(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        file_upload = request.data["file"]
        # print(request.data,request.POST)
        input_data = encode(
            str(request.POST["input"]).encode().decode("unicode_escape"),
            "raw_unicode_escape",
        )
        path = os.path.join(settings.BASE_DIR, "mediafiles", file_upload.name)
        destination = open(path, "wb+")
        for chunk in file_upload.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        run = subprocess.Popen(
            ["python2.7", path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        grep_stdout = run.communicate(input=input_data)[0]
        print(grep_stdout.decode())
        print(run.returncode)
        return Response({"filename": file_upload.name, "output": grep_stdout.decode()})


class Python38Compiler(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        file_upload = request.data["file"]
        # print(request.data,request.POST)
        input_data = encode(
            str(request.POST["input"]).encode().decode("unicode_escape"),
            "raw_unicode_escape",
        )
        path = os.path.join(settings.BASE_DIR, "mediafiles", file_upload.name)
        destination = open(path, "wb+")
        for chunk in file_upload.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        run = subprocess.Popen(
            ["python3.8", path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        grep_stdout = run.communicate(input=input_data)[0]
        print(grep_stdout.decode())
        print(run.returncode)
        return Response({"filename": file_upload.name, "output": grep_stdout.decode()})


class PHP7Compiler(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        file_upload = request.data["file"]
        # print(request.data,request.POST)
        input_data = encode(
            str(request.POST["input"]).encode().decode("unicode_escape"),
            "raw_unicode_escape",
        )
        path = os.path.join(settings.BASE_DIR, "mediafiles", file_upload.name)
        out = os.path.join(settings.BASE_DIR, "mediafiles")
        destination = open(path, "wb+")
        for chunk in file_upload.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        run = subprocess.Popen(
            ["php", path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        grep_stdout = run.communicate(input=input_data)[0]
        print(grep_stdout.decode())
        print(run.returncode)
        return Response({"filename": file_upload.name, "output": grep_stdout.decode()})


class CCompiler(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        file_upload = request.data["file"]
        # print(request.data,request.POST)
        input_data = encode(
            str(request.POST["input"]).encode().decode("unicode_escape"),
            "raw_unicode_escape",
        )
        path = os.path.join(settings.BASE_DIR, "mediafiles", file_upload.name)
        out = os.path.splitext(path)[0]
        destination = open(path, "wb+")
        for chunk in file_upload.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        run1 = subprocess.Popen(
            ["cc", path, "-o", out],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        grep_stdout1 = run1.communicate(input=b"")[0]
        if run1.returncode == 0:
            run2 = subprocess.Popen(
                [out],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            grep_stdout2 = run2.communicate(input=input_data)[0]
            output = grep_stdout2.decode()
            # print(run1.returncode,run2.returncode)
        else:
            output = grep_stdout1.decode()
        return Response({"filename": file_upload.name, "output": output})


class CPlusPlusCompiler(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        file_upload = request.data["file"]
        # print(request.data,request.POST)
        input_data = encode(
            str(request.POST["input"]).encode().decode("unicode_escape"),
            "raw_unicode_escape",
        )
        path = os.path.join(settings.BASE_DIR, "mediafiles", file_upload.name)
        out = os.path.splitext(path)[0]
        destination = open(path, "wb+")
        for chunk in file_upload.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        run1 = subprocess.Popen(
            ["c++", path, "-o", out],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        grep_stdout1 = run1.communicate(input=b"")[0]
        if run1.returncode == 0:
            run2 = subprocess.Popen(
                [out],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            grep_stdout2 = run2.communicate(input=input_data)[0]
            output = grep_stdout2.decode()
            # print(run1.returncode,run2.returncode)
        else:
            output = grep_stdout1.decode()
        return Response({"filename": file_upload.name, "output": output})


class Java8Compiler(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        file_upload = request.data["file"]
        # print(request.data,request.POST)
        input_data = encode(
            str(request.POST["input"]).encode().decode("unicode_escape"),
            "raw_unicode_escape",
        )
        path = os.path.join(settings.BASE_DIR, "mediafiles", file_upload.name)
        out = os.path.join(settings.BASE_DIR, "mediafiles")
        destination = open(path, "wb+")
        for chunk in file_upload.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        run1 = subprocess.Popen(
            ["javac8", path, "-d", out],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        grep_stdout1 = run1.communicate(input=b"")[0]
        if run1.returncode == 0:
            run2 = subprocess.Popen(
                ["java8", "-cp", out, "Solution"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            grep_stdout2 = run2.communicate(input=input_data)[0]
            output = grep_stdout2.decode()
            print(1, output)
            # print(run1.returncode,run2.returncode)
        else:
            output = grep_stdout1.decode()
            print(2, output)
        return Response({"filename": file_upload.name, "output": output})


class Java11Compiler(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        file_upload = request.data["file"]
        # print(request.data,request.POST)
        input_data = encode(
            str(request.POST["input"]).encode().decode("unicode_escape"),
            "raw_unicode_escape",
        )
        path = os.path.join(settings.BASE_DIR, "mediafiles", file_upload.name)
        out = os.path.join(settings.BASE_DIR, "mediafiles")
        destination = open(path, "wb+")
        for chunk in file_upload.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        run1 = subprocess.Popen(
            ["javac11", path, "-d", out],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        grep_stdout1 = run1.communicate(input=b"")[0]
        if run1.returncode == 0:
            run2 = subprocess.Popen(
                ["java11", "-cp", out, "Solution"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            grep_stdout2 = run2.communicate(input=input_data)[0]
            output = grep_stdout2.decode()
            # print(run1.returncode,run2.returncode)
        else:
            output = grep_stdout1.decode()
        return Response({"filename": file_upload.name, "output": output})

