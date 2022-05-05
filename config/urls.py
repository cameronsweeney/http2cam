from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/api/', include('rest_framework.urls')), # adds login to browsable API
    path('admin/token/', include('dj_rest_auth.urls')),
    path('pokedex/', include('pokedex.urls')),
    path('', include('homepage.urls'))
]
