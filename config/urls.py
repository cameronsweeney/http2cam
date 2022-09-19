from django.contrib import admin
from django.urls import path, include
from .csrf import csrf, GetCSRFTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csrf/', GetCSRFTokenView.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')), 
    path('apilogin/', include('rest_framework.urls')), # adds login to browsable API
    path('cams/', include('cams.urls')),
    path('pokedex/', include('pokedex.urls')),
    path('', include('homepage.urls'))
]
