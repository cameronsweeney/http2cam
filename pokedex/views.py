from rest_framework import generics, permissions
from .models import PkmnSpecies
from .serializers import PkmnSpeciesSerializer

class ListPkmnSpecies(generics.ListAPIView):
    queryset = PkmnSpecies.objects.all()
    serializer_class = PkmnSpeciesSerializer

class DetailPkmnSpecies(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly)
    queryset = PkmnSpecies.objects.all()
    serializer_class = PkmnSpeciesSerializer