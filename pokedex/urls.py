from django.contrib import admin
from django.urls import path
from .views import ListPkmnSpecies, DetailPkmnSpecies

urlpatterns = [
    path('<int:pk>/', ListPkmnSpecies.as_view()),
   #path('<str:species>/', Name_PkmnSpeciesViewSet.as_view()),
    path('', DetailPkmnSpecies.as_view())
]
