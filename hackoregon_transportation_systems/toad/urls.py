from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from toad import views

router = DefaultRouter()
router.register(
    r"busAmRushSummary", views.BusAmRushSummaryViewSet, basename="bus-am-rush-summary"
)
router.register(
    r"busPmRushSummary", views.BusPmRushSummaryViewSet, basename="bus-pm-rush-summary"
)
router.register(
    r"busSystemWideSummary",
    views.BusSystemWideSummaryViewSet,
    basename="bus-system-wide-summary",
)
router.register(
    r"busByStopSummary", views.BusByStopSummaryViewSet, basename="bus-by-stop-summary"
)
router.register(
    r"busPassengerStops", views.BusPassengerStopsViewSet, basename="bus-passenger-stops"
)
router.register(
    r"busPassengerStopsCatalog",
    views.BusPassengerStopsCatalogViewSet,
    basename="bus-passenger-stops-catalog"
)
router.register(
    r"railAmRushSummary", views.RailAmRushSummaryViewSet, basename="rail-am-rush-summary"
)
router.register(
    r"railPmRushSummary", views.RailPmRushSummaryViewSet, basename="rail-pm-rush-summary"
)
router.register(
    r"railSystemWideSummary",
    views.RailSystemWideSummaryViewSet,
    basename="rail-system-wide-summary",
)
router.register(
    r"railByStopSummary", views.RailByStopSummaryViewSet, basename="rail-by-stop-summary"
)
router.register(
    r"railPassengerStops",
    views.RailPassengerStopsViewSet,
    basename="rail-passenger-stops",
)
router.register(
    r"railPassengerStopsCatalog",
    views.RailPassengerStopsCatalogViewSet,
    basename="rail-passenger-stops-catalog",
)
router.register(
    r"disturbanceStops", views.DisturbanceStopsViewSet, basename="disturbance-stops"
)
router.register(
    r"disturbanceStopsCatalog",
    views.DisturbanceStopsCatalogViewSet,
    basename="disturbance-stops-catalog"
)
router.register(
    r"disturbanceSystemWideSummary",
    views.DisturbanceSystemWideSummaryViewSet,
    basename="disturbance-system-wide-summary",
)
router.register(
    r"trafficSignals", views.TrafficSignalsViewSet, basename="traffic-signals"
)
router.register(
    r"passengerStopLocations",
    views.PassengerStopLocationsViewSet,
    basename="passenger-stop-stop-locations",
)
router.register(r"tmRailStops", views.TmRailStopsViewSet, basename="tm-rail-stops")
router.register(r"tmRouteStops", views.TmRouteStopsViewSet, basename="tm-route-stops")
router.register(
    r"ncdbSampleTransportationCommutes",
    views.NcdbSampleTransportationCommuteViewSet,
    basename="ncdb-sample-transportation-commutes",
)
router.register(
    r"BusstopCatchmentZoneWithCensusAttribs",
    views.BusstopCatchmentZoneWithCensusAttribsViewSet,
    basename="bus-stop-catchment-zone-with-census-attribs",
)

urlpatterns = [url(r"^", include(router.urls))]
