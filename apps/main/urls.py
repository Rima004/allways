from django.urls import path


from apps.main.views import MainView, MapsView, StatisticsView, donate_view

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("maps/", MapsView.as_view(), name="maps"),
    path("statistics/", StatisticsView.as_view(), name="statistics"),
    path("donate/",donate_view, name="donate"),
]
