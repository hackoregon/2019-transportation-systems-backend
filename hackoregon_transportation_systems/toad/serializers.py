# from rest_framework import serializers
from rest_framework_gis import serializers
from toad.models import (
    DisturbanceStops,
    TrafficSignals,
    BusAllStops,
    BusPassengerStops,
    RailPassengerStops,
    TmRouteStops,
    TmRailStops,
)


class BusAllStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = BusAllStops
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class BusPassengerStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = BusPassengerStops
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class RailPassengerStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = RailPassengerStops
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class DisturbanceStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = DisturbanceStops
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class TrafficSignalsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = TrafficSignals
        fields = ("wkb_geometry", "ogc_fid")
        geo_field = "wkb_geometry"
        id = "ogc_fid"


class TmRouteStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = TmRouteStops
        fields = "__all__"
        geo_field = "wkb_geometry"
        id = "ogc_fid"


class TmRailStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = TmRailStops
        fields = "__all__"
        geo_field = "wkb_geometry"
        id = "ogc_fid"
