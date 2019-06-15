from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from toad import views

router = DefaultRouter()
router.register(r"busAllStops", views.BusAllStopsViewSet, basename="bus-all-stops")
router.register(
    r"busPassengerStops", views.BusPassengerStopsViewSet, basename="bus-passenger-stops"
)
router.register(
    r"""^DisturbanceStops/
    (?P<line>[0-9]+)
    (?P<direction>[A-Z]+)
    (?P<num>[0-9]+)
    (?P<start_quarter_hour>[0-9]*\.?[0-9]+)
    (?P<end_quarter_hour>[0-9]*\.?[0-9]+)
    (?P<start_month>[A-Z]+)
    (?P<end_month>[A-Z]+)
    (?P<year>[A-Z]+)/$""",
    views.DisturbanceStopsViewSet,
    basename="disturbance-stops",
)
router.register(
    r"trafficSignals", views.TrafficSignalsViewSet, basename="traffic-signals"
)

urlpatterns = [url(r"^", include(router.urls))]
