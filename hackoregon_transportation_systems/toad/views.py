import coreapi
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from toad.models import (
    BusAllStops,
    BusPassengerStops,
    RailPassengerStops,
    DisturbanceStops,
    TrafficSignals,
)
from toad.serializers import (
    BusAllStopsSerializer,
    BusPassengerStopsSerializer,
    RailPassengerStopsSerializer,
    DisturbanceStopsSerializer,
    TrafficSignalsSerializer,
)


class BusAllStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of all times a bus stops (scheduled or not).
    """

    queryset = BusAllStops.objects.all()
    serializer_class = BusAllStopsSerializer


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
                description="Bus routes to include. Example: '10,14' for routes 10 and 14.",
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
                description="Service Key ('W' - Weekday, 'S' - Saturday, 'U' - Sunday, 'X' - Holiday).",
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


class BusPassengerStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will query scheduled stops along a Trimet bus line.
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
            filters["route_number__in"] = [int(l) for l in lines.split(",")]

        stops = self.request.query_params.get("stops", False)
        if stops:
            filters["location_id__in"] = [int(s) for s in stops.split(",")]

        directions = self.request.query_params.get("directions", False)
        if directions:
            filters["direction__in"] = [int(d) for d in directions.split(",")]

        service_key = self.request.query_params.get("service_key", False)
        if service_key:
            filters["service_key__in"] = [sk for sk in service_key.split(",")]

        time_range = self.request.query_params.get("time_range", False)
        if time_range:
            times = [float(time) for time in time_range.split(",")]
            r = [times[0], times[1]]
            filters["arrive_quarter_hour__range"] = r

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
    This viewset will provide a list of scheduled stops along a Trimet rail line.
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
            filters["route_number__in"] = [int(l) for l in lines.split(",")]

        stops = self.request.query_params.get("stops", False)
        if stops:
            filters["location_id__in"] = [int(s) for s in stops.split(",")]

        directions = self.request.query_params.get("directions", False)
        if directions:
            filters["direction__in"] = [int(d) for d in directions.split(",")]

        service_key = self.request.query_params.get("service_key", False)
        if service_key:
            filters["service_key__in"] = [sk for sk in service_key.split(",")]

        time_range = self.request.query_params.get("time_range", False)
        if time_range:
            times = [float(time) for time in time_range.split(",")]
            r = [times[0], times[1]]
            filters["arrive_quarter_hour__range"] = r

        queryset = RailPassengerStops.objects.filter(**filters)

        return queryset


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
                required=False,
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
                required=False,
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
    This viewset will provide a list of all disturbance stops of busses.
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
        if months:
            filters["month__in"] = [int(m) for m in months.split(",")]

        years = self.request.query_params.get("years", False)
        if years:
            filters["year__in"] = [int(y) for y in years.split(",")]

        lines = self.request.query_params.get("lines", False)
        if lines:
            filters["line_id__in"] = [int(l) for l in lines.split(",")]

        directions = self.request.query_params.get("directions", False)
        if directions:
            filters["pattern_direction__in"] = [d for d in directions.split(",")]

        service_key = self.request.query_params.get("service_key", False)
        if service_key:
            filters["service_key__in"] = [sk for sk in service_key.split(",")]

        time_range = self.request.query_params.get("time_range", False)
        if time_range:
            times = [float(time) for time in time_range.split(",")]
            r = [times[0], times[1]]
            filters["start_quarter_hour__range"] = r
            filters["end_quarter_hour__range"] = r

        bounds = self.request.query_params.get("bounds", False)
        if bounds:
            min_lon, min_lat, max_lon, max_lat = [float(b) for b in bounds.split(",")]
            filters["latitude__range"] = [min_lat, max_lat]
            filters["longitude__range"] = [min_lon, max_lon]

        num = self.request.query_params.get("num", False)
        if num:
            queryset = DisturbanceStops.objects.filter(**filters)[: int(num)]
        else:
            queryset = DisturbanceStops.objects.filter(**filters)

        return queryset


class TrafficSignalsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of all the traffic signals in the Portland area.
    """

    queryset = TrafficSignals.objects.all()
    serializer_class = TrafficSignalsSerializer
