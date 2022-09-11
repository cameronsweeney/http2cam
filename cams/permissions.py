# cams/permissions.py
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, exceptions
from rest_framework_yaml.encoders import SafeDumper
from yaml.representer import SafeRepresenter
from .models import CamsAppAuthorization, CamsFileTree, CamsModel, CamsApp

class CamsAppPermission(permissions.DjangoObjectPermissions):
    def has_object_permission(self, request, view, app_name):
        SafeDumper.add_representer(exceptions.ErrorDetail, SafeRepresenter.represent_str)
        obj = CamsAppAuthorization.objects.filter(user=request.user.id, app=app_name)
        if obj.exists():
            return True
        else:
            return False

class CamsModelPermission(permissions.DjangoObjectPermissions):
    def has_object_permission(self, request, view, model_name):
        SafeDumper.add_representer(exceptions.ErrorDetail, SafeRepresenter.represent_str)
        try:
            model = CamsModel.objects.select_related('app').filter(codename=model_name).get()
            obj = CamsAppAuthorization.objects.filter(user=request.user.id, app=model.app_id)
        except ObjectDoesNotExist:
            return False
        if obj.exists():
            return True
        else:
            return False

class CamsFileTreePermission(permissions.DjangoObjectPermissions):
    def has_object_permission(self, request, view, filetree_name):
        SafeDumper.add_representer(exceptions.ErrorDetail, SafeRepresenter.represent_str)
        try:
            filetree = CamsFileTree.objects.select_related('app').filter(codename=filetree_name).get()
            obj = CamsAppAuthorization.objects.filter(user=request.user.id, app=filetree.app_id)
        except ObjectDoesNotExist:
            return False
        if obj.exists():
            return True
        else:
            return False

class CamsCRUDPermission(permissions.DjangoObjectPermissions):
    def has_object_permission(self, request, view, obj):
        SafeDumper.add_representer(exceptions.ErrorDetail, SafeRepresenter.represent_str)
        try:
            app_authorization = CamsAppAuthorization.objects.filter(user=request.user.id, app=obj.cams_model.app)
        except ObjectDoesNotExist:
            return False
        if app_authorization.exists():
            return True
        else:
            return False