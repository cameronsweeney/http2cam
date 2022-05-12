from django.contrib import admin
from . import meta, moves, pkmn, items

admin.site.register(meta.Game)
admin.site.register(meta.Type)

admin.site.register(pkmn.PkmnSpecies)
admin.site.register(pkmn.Evolution)
admin.site.register(pkmn.Pkmn_RBY)

admin.site.register(moves.Move)
admin.site.register(moves.LevelupMove)

admin.site.register(items.Item)