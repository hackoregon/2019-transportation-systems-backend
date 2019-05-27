from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()

schema_view = get_swagger_view(title="Hack Oregon Transportation Systems 2019 API")


urlpatterns = [
    url(r"^transportation-systems/schema/", schema_view),
    url(
        r"^transportation-systems/toad/",
        include("hackoregon_transportation_systems.toad.urls"),
    ),
]
