from django.db import models
from rest_framework import serializers, viewsets, permissions

class Item(models.Model):
    name = models.CharField(max_length=25)
    id = models.PositiveSmallIntegerField(primary_key=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    effect = models.TextField(blank=True)

    def __str__(self):
        return f"Item: {self.name}"

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'id', 'price', 'effect')

class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer