from django.contrib import admin
from django.urls import path
from .views import ListPkmnSpecies, DetailPkmnSpecies_by_ID, DetailPkmnSpecies_by_name

urlpatterns = [
    path('<int:pk>/', DetailPkmnSpecies_by_ID.as_view()),
    path('<str:species>/', DetailPkmnSpecies_by_name.as_view()),
    path('', ListPkmnSpecies.as_view())
]
