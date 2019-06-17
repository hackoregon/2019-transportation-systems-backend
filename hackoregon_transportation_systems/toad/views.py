import coreapi
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from toad.models import BusAllStops, BusPassengerStops, DisturbanceStops, TrafficSignals
from toad.serializers import (
    BusAllStopsSerializer,
    BusPassengerStopsSerializer,
    DisturbanceStopsSerializer,
    TrafficSignalsSerializer,
)


class BusAllStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of all times a bus stops (scheduled or not).
    """

    queryset = BusAllStops.objects.all()
    serializer_class = BusAllStopsSerializer


class BusPassengerStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of scheduled stops along a Trimet line.
    """

    queryset = BusPassengerStops.objects.all()
    serializer_class = BusPassengerStopsSerializer


class DisturbanceStopsFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into schema.
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
                description="Months to filter on. Example: 9,10,11 to include September, October and November.",
            ),
            coreapi.Field(
                name="time_range",
                required=False,
                location="query",
                type="string",
                description="Quarter hour time range to filter on. 6.25,9.5 = 6:15 - 9:30",
            ),
            coreapi.Field(
                name="years",
                required=False,
                location="query",
                type="string",
                description="Years to filter on. Example: 2017",
            ),
            coreapi.Field(
                name="directions",
                required=False,
                location="query",
                type="string",
                description="Line direction. 'I' for Inbound, 'O' for Outbound.",
            ),
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Bus routes to include.",
            ),
            coreapi.Field(
                name="num",
                required=False,
                location="query",
                type="integer",
                description="Number of results to return so that the API doesn't hang.",
            ),
        ]
        return fields


class DisturbanceStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of all disturbance stops of busses.
    """

    # queryset = DisturbanceStops.objects.all()
    serializer_class = DisturbanceStopsSerializer
    filter_backends = (DisturbanceStopsFilter,)

    def get_queryset(self):
        """
        Optionally filters against query parameters in the URL.
        """
        # queryset = DisturbanceStops.objects.all()

        print(self.request.query_params)
        filters = {}
        # really could use the assignment operator here :)
        months = self.request.query_params.get("months", False)
        if months:
            filters["opd_date__month__in"] = [int(m) for m in months.split(",")]

        years = self.request.query_params.get("years", False)
        if years:
            filters["opd_date__year__in"] = [int(y) for y in years.split(",")]

        lines = self.request.query_params.get("lines", False)
        if lines:
            filters["line_id__in"] = [int(l) for l in lines.split(",")]

        directions = self.request.query_params.get("directions", False)
        if directions:
            filters["pattern_direction__in"] = [d for d in directions.split(",")]

        time_range = self.request.query_params.get("time_range", False)
        if time_range:
            times = [float(time) for time in time_range.split(",")]
            r = [times[0], times[1]]
            filters["start_quarter_hour__range"] = r
            filters["end_quarter_hour__range"] = r

        print(filters)
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
