import json

from django.shortcuts import render

from apps.main.models import Places


def main_view(request):
    return render(request, "main.html")


def maps_view(request):
    places = list(Places.objects.values())
    return render(request, "maps.html", {"places": json.dumps(places)})
