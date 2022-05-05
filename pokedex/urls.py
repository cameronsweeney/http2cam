from django.urls import path
from rest_framework import routers
from .views import PkmnSpeciesViewSet, PkmnSpecies_by_name

urlpatterns = [
    path('<str:name>', PkmnSpecies_by_name.as_view())
]

router = routers.SimpleRouter()
router.register('', PkmnSpeciesViewSet, basename='pkmn')

urlpatterns += router.urls