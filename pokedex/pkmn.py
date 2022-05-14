from django.db import models
from rest_framework import serializers, viewsets, permissions, generics
from . import meta

class PkmnSpecies(models.Model):
    natdex = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, unique=True, null=True)
    name_url = models.CharField(max_length=25, unique=True, null=True) # lowercase/no-punctuation version of name to use in URL
    
    pronunciation = models.CharField(max_length=25, blank=True)  # give in IPA unicode
    pronounce_anime_URL = models.CharField(max_length=200, blank=True) # URL link to clip where they say the Pokémon's name in the anime
    
    class Meta:
        verbose_name = verbose_name_plural = 'Pokémon species'

    def __str__(self):
        return f"#{str(self.natdex).zfill(3)}: {self.name}"

class PkmnSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PkmnSpecies
        fields = ('natdex', 'name', 'name_url', 'pronunciation', 'pronounce_anime_URL')

class PkmnSpeciesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = PkmnSpecies.objects.all().order_by('natdex')
    serializer_class = PkmnSpeciesSerializer

class PkmnSpecies_by_name(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = PkmnSpecies.objects.all()
    serializer_class = PkmnSpeciesSerializer
    lookup_field = 'name_url'

class Pkmn_RBY(models.Model):
    # RBY's internal ID for this species
    id = models.PositiveSmallIntegerField(primary_key=True)
    pkmn = models.ForeignKey(PkmnSpecies, to_field='name', db_column='pkmn', on_delete=models.SET_NULL, null=True)

    type1 = models.ForeignKey(meta.Type, on_delete=models.SET_NULL, null=True, related_name='type_one')
    type2 = models.ForeignKey(meta.Type, on_delete=models.SET_NULL, null=True, related_name='type_two', blank=True)

    hp = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    special = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()

    catch_rate = models.PositiveSmallIntegerField()
    base_exp = models.PositiveSmallIntegerField()
    growth_rate = models.CharField(max_length=20)

    tmhm_bits = models.BinaryField()

    class Meta:
        verbose_name = verbose_name_plural = 'Pokémon species data, RBY'

class Pkmn_RBY_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pkmn_RBY
        fields = ('pkmn', 'id', 'type1', 'type2',
            'hp', 'attack', 'defense', 'special', 'speed',
            'catch_rate', 'base_exp', 'growth_rate', 'tmhm_bits'
            )

class Pkmn_RBY_ViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Pkmn_RBY.objects.all()
    serializer_class = Pkmn_RBY_Serializer

class Evolution(models.Model):
    id = models.SmallAutoField(primary_key=True)
    pkmn = models.ForeignKey(PkmnSpecies, on_delete=models.CASCADE, related_name='pkmn_from')
    into = models.ForeignKey(PkmnSpecies, on_delete=models.CASCADE, related_name='pkmn_into')
    how = models.CharField(max_length=200, blank=True)
    when = models.PositiveSmallIntegerField(blank=True)

class EvolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = ('pkmn', 'into', 'how', 'when')

class EvolutionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Evolution.objects.all()
    serializer_class = EvolutionSerializer
