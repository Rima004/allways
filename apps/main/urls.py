from django.urls import path

from apps.main.views import MainView, MapsView, StatisticsView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("maps/", MapsView.as_view(), name="maps"),
    path("statistics/", StatisticsView.as_view(), name="statistics"),
]
