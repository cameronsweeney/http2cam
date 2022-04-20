from django.contrib import admin
from django.urls import path
from .views import ListPkmnSpecies, DetailPkmnSpecies

urlpatterns = [
    path('<int:pk>/', DetailPkmnSpecies.as_view()),
    path('', ListPkmnSpecies.as_view())
]
