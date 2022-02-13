from django.http import HttpResponse, JsonResponse
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
    response = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }

    }
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
