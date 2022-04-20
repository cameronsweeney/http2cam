from django.contrib import admin
from .models import myUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(myUser, UserAdmin)