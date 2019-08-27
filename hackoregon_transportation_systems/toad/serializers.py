# from rest_framework import serializers
from rest_framework_gis import serializers
from toad.models import (
    DisturbanceStops,
    DisturbanceSystemWideSummary,
    TrafficSignals,
    BusPassengerStops,
    RailPassengerStops,
    TmRouteStops,
    TmRailStops,
    BusAmRushSummary,
    BusPmRushSummary,
    BusSystemWideSummary,
    BusByStopSummary,
    RailAmRushSummary,
    RailPmRushSummary,
    RailSystemWideSummary,
    RailByStopSummary,
    PassengerStopLocations
)


class BusAmRushSummarySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = BusAmRushSummary
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class BusPmRushSummarySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = BusPmRushSummary
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class BusSystemWideSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSystemWideSummary
        fields = "__all__"
        id = "arrive_quarter_hour"


class BusByStopSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusByStopSummary
        fields = "__all__"
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


class RailAmRushSummarySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = RailAmRushSummary
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class RailPmRushSummarySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = RailPmRushSummary
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class RailByStopSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = RailByStopSummary
        fields = "__all__"
        id = "id"


class DisturbanceStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = DisturbanceStops
        fields = "__all__"
        geo_field = "geom_point_4326"
        id = "id"


class DisturbanceSystemWideSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DisturbanceSystemWideSummary
        fields = "__all__"
        id = "start_quarter_hour"


class RailSystemWideSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = RailSystemWideSummary
        fields = "__all__"
        id = "arrive_quarter_hour"


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


class PassengerStopLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerStopLocations
        fields = "__all__"
        id = "stop_id"
