from rest_framework import generics
from .models import PkmnSpecies
from .serializers import PkmnSpeciesSerializer

class ListPkmnSpecies(generics.ListAPIView):
    queryset = PkmnSpecies.objects.all()
    serializer_class = PkmnSpeciesSerializer

class DetailPkmnSpecies(generics.RetrieveUpdateDestroyAPIView):
    queryset = PkmnSpecies.objects.all()
    serializer_class = PkmnSpeciesSerializer