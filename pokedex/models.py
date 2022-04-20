from django.db import models

# Create your models here.

class PkmnSpecies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"#{str(self.id).zfill(3)}: {self.name}"