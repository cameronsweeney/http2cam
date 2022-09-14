# cams/serializers.py
from rest_framework import serializers
from . import models

class CamsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CamsModel
        fields = ('codename', 'name', 'fields', 'description')

class CamsActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CamsActionGlobal
        fields = ('codename', 'name', 'description')

class AppInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CamsApp
        fields = ('codename', 'name', 'description')

class AppViewSerializer(serializers.ModelSerializer):
    app = AppInstanceSerializer()

    class Meta:
        model = models.CamsAppAuthorization
        fields = ('app',)
        depth = 1

class CamsModelInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CamsModelInstance
        fields = ('filepath', 'id', 'content')
        depth = 1

class CamsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CamsModel
        fields = ('codename', 'name', 'fields', 'description')

class CamsActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CamsActionGlobal
        fields = ('codename', 'name', 'description')

class CamsFileTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CamsFileTree
        fields = ('name', 'codename', 'app', 'description')