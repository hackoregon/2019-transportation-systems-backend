from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from toad import views

router = DefaultRouter()
router.register(r"bus-all-stops", views.BusAllStopsViewSet)
router.register(r"bus-passenger-stops", views.BusPassengerStopsViewSet)

urlpatterns = [url(r"^/", include(router.urls))]
