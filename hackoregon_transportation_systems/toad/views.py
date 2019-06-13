from rest_framework import viewsets
from toad.models import BusAllStops, BusPassengerStops, DisturbanceStops
from toad.serializers import (
    BusAllStopsSerializer,
    BusPassengerStopsSerializer,
    DisturbanceStopsSerializer,
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


class DisturbanceStopsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of all disturbance stops of busses.
    """

    # queryset = DisturbanceStops.objects.all()
    serializer_class = DisturbanceStopsSerializer

    def get_queryset(self):
        """
        Optionally restricts the disturbance stops by line by filtering against a
        `lines` query parameter in the URL.
        """
        queryset = DisturbanceStops.objects.all()
        lines = self.request.query_params.get("lines", None)
        if lines is not None:
            queryset = queryset.filter(line_id__in=[int(l) for l in lines.split(",")])

        direction = self.request.query_params.get("direction", None)
        if direction is not None:
            queryset = queryset.filter(pattern_direction="I")

        return queryset
