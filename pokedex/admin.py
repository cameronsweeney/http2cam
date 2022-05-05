from django.contrib import admin
from .models import Type, GrowthRate, Move, PkmnSpecies, LevelupMoves, Evolution, Item

# Register your models here.

admin.site.register(Type)
admin.site.register(GrowthRate)
admin.site.register(Move)
admin.site.register(PkmnSpecies)
admin.site.register(LevelupMoves) 
admin.site.register(Evolution)
admin.site.register(Item)