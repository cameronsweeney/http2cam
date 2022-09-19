from django.contrib import admin
from .models import CamsApp, CamsAppAuthorization, CamsFileTree, CamsModel, CamsModelInstance, CamsActionGlobal, CamsActionLocal, CamsFormResponse
# Register your models here.

admin.site.register(CamsApp)
admin.site.register(CamsAppAuthorization)
admin.site.register(CamsModel)
admin.site.register(CamsModelInstance)
admin.site.register(CamsActionGlobal)
admin.site.register(CamsActionLocal)
admin.site.register(CamsFileTree)
admin.site.register(CamsFormResponse)