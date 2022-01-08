from django.db import models


class UkTowns(models.Model):
    name = models.CharField(max_length=45, help_text="town name")
    county = models.CharField(max_length=32)
    country = models.CharField(max_length=16, null=True)
    grid_reference = models.CharField(max_length=8)
    easting = models.IntegerField()
    northing = models.IntegerField()
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    postcode_sector = models.CharField(max_length=44)
    nuts_region = models.CharField(max_length=24)
    type = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} | {self.country}"
