from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokedex/', include('pokedex.urls')),
    path('', include('homepage.urls'))
]
