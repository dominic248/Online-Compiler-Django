from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION
    file_overwrite = True


class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    default_acl = "public"
    file_overwrite = True


class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    default_acl = "private"
    file_overwrite = True
    custom_domain = False


class ProfilePrictureStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION + "/profile_picture"
    default_acl = "public-read"
    file_overwrite = False


class ProductMainPrictureStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION + "/products/main"
    default_acl = "public-read"
    file_overwrite = True
