from django.db import models
from django.conf import settings
import uuid
from datetime import datetime

class CamsApp(models.Model):
    name = models.CharField(max_length=30)
    codename = models.CharField(max_length=30, primary_key=True)
    description = models.TextField(blank=True)

class CamsAppAuthorization(models.Model):
    app = models.ForeignKey(CamsApp, on_delete=models.CASCADE, related_name='app')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CamsModel(models.Model):
    name = models.CharField(max_length=100)
    codename = models.CharField(max_length=30, primary_key=True)
    app = models.ForeignKey(CamsApp, on_delete=models.CASCADE)
    fields = models.JSONField()
    description = models.TextField(blank=True)    

class CamsModelInstance(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=True)
    cams_model = models.ForeignKey(CamsModel, on_delete=models.CASCADE)
    content = models.JSONField()
    filepath = models.TextField(blank=True)

class CamsActionGlobal(models.Model):
    name = models.CharField(max_length=30)
    codename = models.CharField(max_length=30, primary_key=True)
    app = models.ForeignKey(CamsApp, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

class CamsActionLocal(models.Model):
    name = models.CharField(max_length=30)
    codename = models.CharField(max_length=30, primary_key=True)
    cams_model = models.ForeignKey(CamsModel, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    
class CamsFileTree(models.Model):
    name = models.CharField(max_length=30)
    codename = models.CharField(max_length=30, primary_key=True)
    app = models.ForeignKey(CamsApp, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

class CamsFormResponse(models.Model):
    response_data = models.JSONField()
    date = models.DateTimeField(default=datetime.now, blank=True)