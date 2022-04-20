from rest_framework import serializers
from .models import PkmnSpecies

class PkmnSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PkmnSpecies
        fields = ('id', 'name')