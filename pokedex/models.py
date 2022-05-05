from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    name_long = models.CharField(max_length=100, unique=True)
    series = models.CharField(max_length=10)

class Type(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    index = models.PositiveSmallIntegerField()

class GrowthRate(models.Model):
    name = models.CharField(max_length=15, primary_key=True)

class Move(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    id = models.PositiveSmallIntegerField()
    effect = models.TextField()
    power = models.PositiveSmallIntegerField()
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    accuracy = models.PositiveSmallIntegerField()
    pp = models.PositiveSmallIntegerField()

class PkmnSpecies(models.Model):
    natdex = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, unique=True, null=True)
    name_url = models.CharField(max_length=25, unique=True, null=True) # lowercase/no-punctuation version of name to use in URL
    
    pronunciation = models.CharField(max_length=25)  # give in IPA unicode
    pronounce_anime_URL = models.CharField(max_length=200) # URL link to clip where they say the Pokémon's name in the anime
    
    class Meta:
        verbose_name = 'Pokémon species name'

class SpeciesHeader_RBY(models.Model):
    id = models.OneToOneField(PkmnSpecies, primary_key=True, on_delete=models.CASCADE)

    type1 = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name='type_one')
    type2 = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name='type_two')

    hp = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    special = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()

    catch_rate = models.PositiveSmallIntegerField()
    base_exp = models.PositiveSmallIntegerField()
    growth_rate = models.ForeignKey(GrowthRate, on_delete=models.SET_NULL, null=True)

    tmhm_bits = models.BinaryField()

    def __str__(self):
        return f"#{str(self.natdex).zfill(3)}: {self.name}"

    class Meta:
        verbose_name = verbose_name_plural = 'Pokémon species data, RBY'

class LevelupMoves(models.Model):
    pkmn = models.ForeignKey(PkmnSpecies, on_delete=models.SET_NULL, null=True)
    move = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True)
    level = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Level-up Move'

class Evolution(models.Model):
    from_pkmn = models.ForeignKey(PkmnSpecies, on_delete=models.SET_NULL, null=True, related_name='+')
    into_pkmn = models.ForeignKey(PkmnSpecies, on_delete=models.SET_NULL, null=True, related_name='+')
    how = models.TextField()
    when = models.PositiveSmallIntegerField()
    
class Item(models.Model):
    name = models.CharField(max_length=25)
    id = models.PositiveSmallIntegerField(primary_key=True)
    price = models.PositiveIntegerField()
    effect = models.TextField()