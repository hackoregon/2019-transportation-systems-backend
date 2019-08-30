import coreapi
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from toad.models import (
    BusAmRushSummary,
    BusPmRushSummary,
    BusPassengerStops,
    BusByStopSummary,
    BusSystemWideSummary,
    RailPassengerStops,
    RailAmRushSummary,
    RailPmRushSummary,
    RailByStopSummary,
    DisturbanceStops,
    DisturbanceSystemWideSummary,
    TrafficSignals,
    TmRailStops,
    TmRouteStops,
    RailSystemWideSummary,
    PassengerStopLocations
)

from toad.pre_existing_models import NcdbSampleTransportationCommute

from toad.serializers import (
    BusAmRushSummarySerializer,
    BusPmRushSummarySerializer,
    BusPassengerStopsSerializer,
    BusSystemWideSummarySerializer,
    BusByStopSummarySerializer,
    RailPassengerStopsSerializer,
    RailAmRushSummarySerializer,
    RailPmRushSummarySerializer,
    RailByStopSummarySerializer,
    DisturbanceStopsSerializer,
    DisturbanceSystemWideSummarySerializer,
    TrafficSignalsSerializer,
    TmRailStopsSerializer,
    TmRouteStopsSerializer,
    RailSystemWideSummarySerializer,
    PassengerStopLocationsSerializer,
    NcdbSampleTransportationCommuteSerializer
)


class BusPassengerStopsFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = BusPassengerStops

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Bus route numbers to include, separated by a comma.\n\nExample:\t10,14\n\nReturns data for only routes 10 and 14.",
            ),
            coreapi.Field(
                name="stops",
                required=False,
                location="query",
                type="string",
                description="Stop ids to include, separated by a comma.\n\nExample:\tstopid1,stopid2,stopid3\n\nReturns data for only these stops.",
            ),
            coreapi.Field(
                name="time_range",
                required=False,
                location="query",
                type="string",
                description=(
                    "Decimal time range to filter on (24 hour). Formatted as 'START,STOP', where START and STOP are numbers. Both START and STOP are required. The decimal format is converted to correct time format.\n\nExample:\t6.25,9.5\n\nReturns data filtered from 6:15 am to 9:30 am."
                ),
            ),
            coreapi.Field(
                name="service_key",
                required=False,
                location="query",
                type="string",
                description="Service Key\n\nW - Weekdays\nS - Saturday\nU - Sunday\nX - Holiday",
            ),
            coreapi.Field(
                name="directions",
                required=False,
                location="query",
                type="string",
                description="Line direction\n\n1 for Inbound (or often Southbound)\n0 for Outbound (or often Northbound)\n\nExample:\t1,0\n\nReturns data from both directions of a route.",
            ),
        ]

        return fields


class BusAmRushSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Bus AM rush hour summary statistics.
    """

    queryset = BusAmRushSummary.objects.all()
    serializer_class = BusAmRushSummarySerializer


class BusPmRushSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Bus PM rush hour summary statistics.
    """

    queryset = BusPmRushSummary.objects.all()
    serializer_class = BusPmRushSummarySerializer


class BusSystemWideSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Bus System Wide summary statistics.
    """

    queryset = BusSystemWideSummary.objects.all()
    serializer_class = BusSystemWideSummarySerializer


class BusByStopSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Bus By Stop summary statistics.
    """

    queryset = BusByStopSummary.objects.all()
    serializer_class = BusByStopSummarySerializer


class BusPassengerStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points from scheduled stop events along TriMet bus routes.
    """

    serializer_class = BusPassengerStopsSerializer
    filter_backends = (BusPassengerStopsFilter,)

    def get_queryset(self):
        """
        Filters against query parameters in the URL.
        """

        filters = {}
        # really could use the assignment operator here :)
        lines = self.request.query_params.get("lines", False)
        if lines:
            try:
                filters["route_number__in"] = [int(l) for l in lines.split(",")]
            except ValueError:
                raise ValidationError(
                    {"route_number": f"'{lines}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"route_number": f"'{lines}' - unknown error."})

        stops = self.request.query_params.get("stops", False)
        if stops:
            try:
                filters["location_id__in"] = [int(s) for s in stops.split(",")]
            except ValueError:
                raise ValidationError(
                    {"stop_id": f"'{stops}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"stop_id": f"'{stops}' - unknown error."})

        directions = self.request.query_params.get("directions", False)
        if directions:
            try:
                filters["direction__in"] = [int(d) for d in directions.split(",")]
            except ValueError:
                raise ValidationError(
                    {"direction": f"'{directions}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"direction": f"'{directions}' - unknown error."})                

        service_key = self.request.query_params.get("service_key", False)
        if service_key:
            try:
                filters["service_key__in"] = [sk for sk in service_key.split(",")]
            except ValueError:
                raise ValidationError(
                    {"service_key": f"'{service_key}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"service_key": f"'{service_key}' - unknown error."})   

        time_range = self.request.query_params.get("time_range", False)
        if time_range:
            try:
                times = [float(time) for time in time_range.split(",")]
                r = [times[0], times[1]]
                filters["arrive_quarter_hour__range"] = r
            except ValueError:
                raise ValidationError(
                    {"time_range": f"'{time_range}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"time_range": f"'{time_range}' - unknown error."})                   

        queryset = BusPassengerStops.objects.filter(**filters)

        return queryset


class RailPassengerStopsFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = RailPassengerStops

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Rail routes to include. `90` - RED, `100` - BLUE, `190` - YELLOW, `200` - GREEN, `290` - ORANGE. Example: '90,100' for the RED and BLUE lines.",
            ),
            coreapi.Field(
                name="stops",
                required=False,
                location="query",
                type="string",
                description="Stop ids to include. Example:",
            ),
            coreapi.Field(
                name="time_range",
                required=False,
                location="query",
                type="string",
                description="Quarter hour time range to filter on. Example: '6.25,9.5' would filter from 6:15 am to 9:30 am",
            ),
            coreapi.Field(
                name="service_key",
                required=False,
                location="query",
                type="string",
                description="Service Key ('A' - Weekday MAX, 'B' - Saturday MAX, 'C' - Sunday MAX).",
            ),
            coreapi.Field(
                name="directions",
                required=False,
                location="query",
                type="string",
                description="Line direction. '1' for Inbound (or often Southboound), '0' for Outbound (or often Northbound). Example: '1,0'.",
            ),
        ]

        return fields


class RailPassengerStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points from scheduled stop events along TriMet rail routes.
    """

    serializer_class = RailPassengerStopsSerializer
    filter_backends = (RailPassengerStopsFilter,)

    def get_queryset(self):
        """
        Filters against query parameters in the URL.
        """

        filters = {}
        # really could use the assignment operator here :)
        lines = self.request.query_params.get("lines", False)
        if lines:
            try:
                filters["route_number__in"] = [int(l) for l in lines.split(",")]
            except ValueError:
                raise ValidationError(
                    {"route_number": f"'{lines}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"route_number": f"'{lines}' - unknown error."})

        stops = self.request.query_params.get("stops", False)
        if stops:
            try:
                filters["location_id__in"] = [int(s) for s in stops.split(",")]
            except ValueError:
                raise ValidationError(
                    {"stop_id": f"'{stops}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"stop_id": f"'{stops}' - unknown error."})

        directions = self.request.query_params.get("directions", False)
        if directions:
            try:
                filters["direction__in"] = [int(d) for d in directions.split(",")]
            except ValueError:
                raise ValidationError(
                    {"direction": f"'{directions}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"direction": f"'{directions}' - unknown error."})                

        service_key = self.request.query_params.get("service_key", False)
        if service_key:
            try:
                filters["service_key__in"] = [sk for sk in service_key.split(",")]
            except ValueError:
                raise ValidationError(
                    {"service_key": f"'{service_key}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"service_key": f"'{service_key}' - unknown error."})   

        time_range = self.request.query_params.get("time_range", False)
        if time_range:
            try:
                times = [float(time) for time in time_range.split(",")]
                r = [times[0], times[1]]
                filters["arrive_quarter_hour__range"] = r
            except ValueError:
                raise ValidationError(
                    {"time_range": f"'{time_range}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"time_range": f"'{time_range}' - unknown error."})  

        queryset = RailPassengerStops.objects.filter(**filters)

        return queryset


class RailAmRushSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Rail AM rush hour summary statistics.
    """

    queryset = RailAmRushSummary.objects.all()
    serializer_class = RailAmRushSummarySerializer


class RailPmRushSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Rail PM rush hour summary statistics.
    """

    queryset = RailPmRushSummary.objects.all()
    serializer_class = RailPmRushSummarySerializer


class RailByStopSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Rail By Stop summary statistics.
    """

    queryset = RailByStopSummary.objects.all()
    serializer_class = RailByStopSummarySerializer


class RailSystemWideSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Rail System Wide summary statistics.
    """

    queryset = RailSystemWideSummary.objects.all()
    serializer_class = RailSystemWideSummarySerializer


class DisturbanceStopsFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = DisturbanceStops

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="months",
                required=True,
                location="query",
                type="string",
                description="Months to filter on (integer). Only September (9), October (10) and November (11) are available. Example: '9,10' to include September and October.",
            ),
            coreapi.Field(
                name="time_range",
                required=False,
                location="query",
                type="string",
                description="Quarter hour time range to filter on. Example: '6.25,9.5' would filter from 6:15 am to 9:30 am",
            ),
            coreapi.Field(
                name="years",
                required=True,
                location="query",
                type="string",
                description="Years to filter on. Only 2017 and 2018 are available. Example: '2017' or '2017,2018'.",
            ),
            coreapi.Field(
                name="directions",
                required=False,
                location="query",
                type="string",
                description="Line direction. 'I' for Inbound, 'O' for Outbound. Example: 'I,O'.",
            ),
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Bus routes to include. Example: '10,14' for routes 10 and 14.",
            ),
            coreapi.Field(
                name="service_key",
                required=False,
                location="query",
                type="string",
                description="Service Key ('W' - Weekday, 'S' - Saturday, 'U' - Sunday, 'X' - Holiday).",
            ),
            coreapi.Field(
                name="bounds",
                required=False,
                location="query",
                type="string",
                description="Four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). Example: -122.665849,45.510867,-122.653650,45.514367",
            ),
            coreapi.Field(
                name="num",
                required=False,
                location="query",
                type="integer",
                description="Development only. Number of results to return so that the API doesn't hang.",
            ),
        ]
        return fields


class DisturbanceStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points from disturbance stop events along TriMet bus routes.\n
    Disturbance stops are when a bus stops for longer than 5 seconds outside of a scheduled stop catchment area.
    """

    serializer_class = DisturbanceStopsSerializer
    filter_backends = (DisturbanceStopsFilter,)

    def get_queryset(self):
        """
        Filters against query parameters in the URL.
        """
  
        filters = {}
        # really could use the assignment operator here :)
        months = self.request.query_params.get("months", False)
        years = self.request.query_params.get("years", False)
        if months and years:
            filters["month__in"] = [int(m) for m in months.split(",")]
            filters["year__in"] = [int(y) for y in years.split(",")]
        else:
            if not months and not years:
                raise ValidationError({
                    "year": f"'year' - Parameter is required.",
                    "month": f"'month' - Parameter is required."
                    })
            elif not months:
                raise ValidationError({"month": f"'month' - Parameter is required."})
            else:
                raise ValidationError({"year": f"'year' - parameter is required."})

        lines = self.request.query_params.get("lines", False)
        if lines:
            try:
                filters["line_id__in"] = [int(l) for l in lines.split(",")]
            except ValueError:
                raise ValidationError(
                    {"line_id": f"'{lines}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"line_id": f"'{lines}' - unknown error."})   

        directions = self.request.query_params.get("directions", False)
        if directions:
            try:
                filters["pattern_direction__in"] = [d for d in directions.split(",")]
            except ValueError:
                raise ValidationError(
                    {"direction": f"'{lines}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"direction": f"'{lines}' - unknown error."})  

        service_key = self.request.query_params.get("service_key", False)
        if service_key:
            try:
                filters["service_key__in"] = [sk for sk in service_key.split(",")]
            except ValueError:
                raise ValidationError(
                    {"service_key": f"'{service_key}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"service_key": f"'{service_key}' - unknown error."})                  

        time_range = self.request.query_params.get("time_range", False)
        if time_range:
            try:
                times = [float(time) for time in time_range.split(",")]
                r = [times[0], times[1]]
                filters["start_quarter_hour__range"] = r
                filters["end_quarter_hour__range"] = r
            except ValueError:
                raise ValidationError(
                    {"time_range": f"'{time_range}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"time_range": f"'{time_range}' - unknown error."})                       

        bounds = self.request.query_params.get("bounds", False)
        if bounds:
            try:
                min_lon, min_lat, max_lon, max_lat = [float(b) for b in bounds.split(",")]
                filters["latitude__range"] = [min_lat, max_lat]
                filters["longitude__range"] = [min_lon, max_lon]
            except ValueError:
                raise ValidationError(
                    {"bound": f"'{bounds}' is an invalid format."}
                )                    
            except Exception:
                raise ValidationError({"bound": f"'{bounds}' - unknown error."})                 

        num = self.request.query_params.get("num", False)
        if num:
            queryset = DisturbanceStops.objects.filter(**filters)[: int(num)]
        else:
            queryset = DisturbanceStops.objects.filter(**filters)

        return queryset


class DisturbanceSystemWideSummary(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Disturbance System Wide summary statistics.
    """

    queryset = DisturbanceSystemWideSummary.objects.all()
    serializer_class = DisturbanceSystemWideSummarySerializer


class TrafficSignalsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of traffic signal locations in the Portland area.
    """

    queryset = TrafficSignals.objects.all()
    serializer_class = TrafficSignalsSerializer


class TmRouteStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of TriMet bus stop locations in the Trimet service area.
    These locations are current as of early August 2019.
    """

    queryset = TmRouteStops.objects.all()
    serializer_class = TmRouteStopsSerializer


class TmRailStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of TriMet rail stop locations in the Trimet service area.
    These locations are current as of early August 2019.
    """

    queryset = TmRailStops.objects.all()
    serializer_class = TmRailStopsSerializer


class PassengerStopLocations(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Passenger Stop Locations.
    """

    queryset = PassengerStopLocations.objects.all()
    serializer_class = PassengerStopLocationsSerializer

class NcdbSampleTransportationCommuteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Passenger Stop Locations.
    """

    queryset = NcdbSampleTransportationCommute.objects.all()
    serializer_class = NcdbSampleTransportationCommuteSerializer