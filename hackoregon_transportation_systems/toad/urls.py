from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from toad import views

router = DefaultRouter()
router.register(r"bus-all-stops", views.BusAllStopsViewSet)
router.register(r"bus-passenger-stops", views.BusPassengerStopsViewSet)
router.register(
    r"disturbance-stops", views.DisturbanceStopsViewSet, basename="disturbance-stops"
)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(
        r"""^disturbance-stops/
        (?P<line>[0-9]+)
        (?P<direction>[A-Z]+)
        (?P<num>[0-9]+)
        (?P<start_quarter_hour>[0-9]*\.?[0-9]+)
        (?P<end_quarter_hour>[0-9]*\.?[0-9]+)
        (?P<start_month>[A-Z]+)
        (?P<end_month>[A-Z]+)
        (?P<year>[A-Z]+)/$""",
        views.DisturbanceStopsViewSet,
    ),
]
