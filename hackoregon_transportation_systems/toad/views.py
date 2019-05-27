# from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

# from rest_framework.decorators import api_view, detail_route
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
from toad.models import BusAllStops, BusPassengerStops
from toad.serializers import BusAllStopsSerializer, BusPassengerStopsSerializer


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
