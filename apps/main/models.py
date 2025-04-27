from django.db import models


class Places(models.Model):
    name = models.CharField("Name", max_length=500)
    category = models.CharField("Category", max_length=100)
    lat = models.FloatField("Lat")
    lng = models.FloatField("Lng")

    def __str__(self):
        return self.category
