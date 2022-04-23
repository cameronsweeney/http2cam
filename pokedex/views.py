from rest_framework import generics, permissions
from .models import PkmnSpecies
from .serializers import PkmnSpeciesSerializer

class ListPkmnSpecies(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = PkmnSpecies.objects.all().order_by('id')
    serializer_class = PkmnSpeciesSerializer

class DetailPkmnSpecies_by_ID(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = PkmnSpecies.objects.all()
    serializer_class = PkmnSpeciesSerializer

class DetailPkmnSpecies_by_name(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = PkmnSpecies.objects.all()
    serializer_class = PkmnSpeciesSerializer
    lookup_field = 'name'