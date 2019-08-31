from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from toad import views

router = DefaultRouter()
router.register(r"busAmRushSummary", views.BusAmRushSummary, basename="bus-am-rush-summary")
router.register(r"busPmRushSummary", views.BusPmRushSummary, basename="bus-pm-rush-summary")
router.register(r"busSystemWideSummary", views.BusSystemWideSummary, basename="bus-system-wide-summary")
router.register(r"busByStopSummary", views.BusByStopSummary, basename="bus-by-stop-summary")
router.register(
    r"busPassengerStops", views.BusPassengerStopsViewSet, basename="bus-passenger-stops"
)
router.register(
    r"railPassengerStops",
    views.RailPassengerStopsViewSet,
    basename="rail-passenger-stops",
)
router.register(r"passengerStopLocations", views.PassengerStopLocations, basename="passenger-stop-stop-locations")
router.register(r"railAmRushSummary", views.RailAmRushSummary, basename="rail-am-rush-summary")
router.register(r"railPmRushSummary", views.RailPmRushSummary, basename="rail-pm-rush-summary")
router.register(r"railSystemWideSummary", views.RailSystemWideSummary, basename="rail-system-wide-summary")
router.register(r"railByStopSummary", views.RailByStopSummary, basename="rail-by-stop-summary")
router.register(
    r"disturbanceStops", views.DisturbanceStopsViewSet, basename="disturbance-stops"
)
router.register(r"disturbanceSystemWideSummary", views.DisturbanceSystemWideSummary, basename="disturbance-system-wide-summary")
router.register(
    r"trafficSignals", views.TrafficSignalsViewSet, basename="traffic-signals"
)
router.register(r"tmRailStops", views.TmRailStopsViewSet, basename="tm-rail-stops")
router.register(r"tmRouteStops", views.TmRouteStopsViewSet, basename="tm-route-stops")
router.register(r"ncdbSampleTransportationCommutes", views.NcdbSampleTransportationCommuteViewSet, basename="ncdb-sample-transportation-commutes")

urlpatterns = [url(r"^", include(router.urls))]
