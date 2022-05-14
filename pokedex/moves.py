from django.db import models
from rest_framework import serializers, viewsets, permissions
from . import meta, pkmn

class Move(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    name_url = models.CharField(max_length=25, blank=True)
    id = models.PositiveSmallIntegerField(blank=True)
    effect = models.TextField(null=True, blank=True)
    power = models.PositiveSmallIntegerField(blank=True)
    type = models.ForeignKey(meta.Type, on_delete=models.SET_NULL, null=True)
    accuracy = models.PositiveSmallIntegerField(blank=True)
    pp = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Move: {self.name}"

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('name', 'id', 'effect', 'power', 'type', 'accuracy', 'pp')

class MoveViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

class LevelupMove(models.Model):
    pkmn = models.ForeignKey(pkmn.PkmnSpecies, to_field='name', db_column='pkmn', on_delete=models.SET_NULL, null=True)
    move = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True)
    level = models.PositiveSmallIntegerField()
    game = models.ForeignKey(meta.Game, to_field='abbreviation', db_column='game', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Level-up Move'

    def __str__(self):
        start_string = f"{self.pkmn} learns {self.move}"
        if self.level:
            start_string += f"at Lv.{self.level}"
        return start_string + f" ({self.game})"
            

class LevelupMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelupMove
        fields = ('pkmn', 'move', 'level')

class LevelupMoveViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = LevelupMove.objects.all()
    serializer_class = LevelupMoveSerializer