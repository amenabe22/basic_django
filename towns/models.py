from django.db import models
from django.db.models.fields import related


class Country(models.Model):
    name = models.CharField(max_length=45, help_text="country name")

    def __str__(self) -> str:
        return self.name



class CountyName(models.Model):
    name = models.CharField(max_length=45)
    nuts_region = models.CharField(max_length=24)
    type = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class County(models.Model):
    name = models.CharField(max_length=45, help_text="county name")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    county_name = models.ManyToManyField(CountyName)

    def __str__(self) -> str:
        return f"County - {self.name} | Country - {self.country.name}"

# Db model for uk towns


class UkTowns(models.Model):
    name = models.CharField(max_length=45, help_text="town name")
    county = models.CharField(max_length=32)
    country = models.CharField(max_length=16)
    grid_reference = models.CharField(max_length=8)
    easting = models.IntegerField()
    northing = models.IntegerField()
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    postcode_sector = models.CharField(max_length=44)
    nuts_region = models.CharField(max_length=24)
    type = models.CharField(max_length=16)

    def __str__(self):
        return "UkTowns"

