from django.shortcuts import render
from .models import  Places
import  json

# Create your views here.
def main_view(request):
    return render(request,"main.html")

def maps_view(request):
    places = list(Places.objects.values())
    return render(request,"maps.html",{'places': json.dumps(places)})