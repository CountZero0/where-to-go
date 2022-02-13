from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from places.models import Place


def index(request):
    value = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
                }
            }
            for place in Place.objects.all()
        ]
    }

    return render(request, 'places/index.html', context={'geojson': value})


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return HttpResponse(place.title)
