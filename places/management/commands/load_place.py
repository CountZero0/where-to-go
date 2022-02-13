from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import os

import requests

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Load new place'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_description = response.json()

        new_place, _ = Place.objects.get_or_create(
            title=place_description['title'],
            defaults={
                "description_short": place_description['description_short'],
                "description_long": place_description['description_long'],
                "lng": place_description['coordinates']['lng'],
                "lat": place_description['coordinates']['lat']
            }
        )

        for position, image_link in enumerate(place_description["imgs"]):
            response = requests.get(image_link)
            response.raise_for_status()

            new_image, _ = Image.objects.get_or_create(
                place=new_place,
                position=position
            )

            new_image.image.save(
                os.path.basename(response.url), ContentFile(response.content), save=True
            )
