from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, null=True)
    description_short = models.TextField(null=True)
    description_long = models.TextField(null=True)
    lng = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    def __str__(self):
        return self.title
