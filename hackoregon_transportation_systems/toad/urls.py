from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from toad import views

router = DefaultRouter()
router.register(r"busAllStops", views.BusAllStopsViewSet, basename="bus-all-stops")
router.register(
    r"busPassengerStops", views.BusPassengerStopsViewSet, basename="bus-passenger-stops"
)
router.register(
    r"disturbanceStops", views.DisturbanceStopsViewSet, basename="disturbance-stops"
)
router.register(
    r"trafficSignals", views.TrafficSignalsViewSet, basename="traffic-signals"
)

urlpatterns = [url(r"^", include(router.urls))]
