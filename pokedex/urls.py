from django.contrib import admin
from django.urls import path
from .views import PkmnSpeciesViewSet, Name_PkmnSpeciesViewSet

urlpatterns = [
    path('<int:pk>/', PkmnSpeciesViewSet.as_view()),
    path('<str:species>/', Name_PkmnSpeciesViewSet.as_view()),
    path('', PkmnSpeciesViewSet.as_view())
]
