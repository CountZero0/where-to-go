from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, null=True)
    description_short = models.TextField(null=True)
    description_long = HTMLField(null=True)
    lng = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              related_name='images')
    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Позиция"
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.place}"
