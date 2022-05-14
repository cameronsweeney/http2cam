from django.db import models
from rest_framework import serializers, permissions, viewsets

class Game(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    name_long = models.CharField(max_length=100, blank=True)
    abbreviation = models.CharField(max_length=20, blank=True, unique=True)
    gen = models.PositiveSmallIntegerField(blank=True)
    series = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Game: {self.name_long} ({self.abbreviation})"

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'name_long', 'gen', 'series')

class GameViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class Type(models.Model):
    name_url = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"Type: {self.name}"

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name_url', 'name')

class TypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer