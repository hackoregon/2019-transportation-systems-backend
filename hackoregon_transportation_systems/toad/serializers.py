from rest_framework import serializers
from rest_framework_gis import serializers
from toad.models import BusAllStops, BusPassengerStops


class BusAllStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = BusAllStops
        fields = "__all__"
        geo_field = "geom_4326"
        id = "id"


class BusPassengerStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = BusPassengerStops
        fields = "__all__"
        geo_field = "geom_4326"
        id = "id"
