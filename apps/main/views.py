import json

from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.main.models import Places
from apps.main.models import Statistics


def main_view(request):
    return render(request, "main.html")


def maps_view(request):
    places = list(Places.objects.values())
    return render(request, "maps.html", {"places": json.dumps(places)})


def statistics_view(request):
    statist = list(Statistics.objects.values())
    return render(request, "statistics.html", {"statistics": json.dumps(statist)})


class MainView(TemplateView):
    template_name = "main.html"


class MapsView(ListView):
    model = Places
    template_name = "maps.html"
    context_object_name = "places"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["places"] = list(self.get_queryset().values())
        return context


class StatisticsView(ListView):
    model = Statistics
    template_name = "statistics.html"
    context_object_name = "statistics"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["statistics"] = list(self.get_queryset().values())
        return context
