from django.contrib import admin

# Register your models here.


from .forms import *
from import_export.admin import ImportExportModelAdmin
from .models import Addresses
from django.contrib.auth import get_user_model

Users = get_user_model()


@admin.register(Users)
class UsersAdmin(ImportExportModelAdmin):
    pass


@admin.register(Addresses)
class AddressesAdmin(ImportExportModelAdmin):
    pass
