from django.urls import path
from rest_framework import routers
from . import meta, pkmn, moves, items 

urlpatterns = [
    path('<str:name_url>', pkmn.PkmnSpecies_by_name.as_view()),
]

router = routers.SimpleRouter()

router.register('games', meta.GameViewSet, basename='games')
router.register('types', meta.TypeViewSet, basename='types')

router.register('pkmn/rby', pkmn.Pkmn_RBY_ViewSet, basename='pkmn_rby')
router.register('pkmn/evolutions', pkmn.EvolutionViewSet, basename='evolutions')
router.register('pkmn', pkmn.PkmnSpeciesViewSet)

router.register('moves/levelup', moves.LevelupMoveViewSet)
router.register('moves', moves.MoveViewSet, basename='moves')

router.register('items', items.ItemViewSet, basename='items')

router.register('', pkmn.PkmnSpeciesViewSet, basename='pokedex')

urlpatterns += router.urls