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
    url(r"^disturbance-stops/(?P<line>[0-9]+)/$", views.DisturbanceStopsViewSet),
]
