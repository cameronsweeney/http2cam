from rest_framework import generics, permissions, viewsets
from .models import PkmnSpecies
from .serializers import PkmnSpeciesSerializer

class PkmnSpeciesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = PkmnSpecies.objects.all().order_by('natdex')
    serializer_class = PkmnSpeciesSerializer

class PkmnSpecies_by_name(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = PkmnSpecies.objects.all()
    serializer_class = PkmnSpeciesSerializer
    lookup_field = 'name'