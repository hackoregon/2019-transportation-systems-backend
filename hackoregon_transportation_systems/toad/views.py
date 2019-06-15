from rest_framework import viewsets
from toad.models import BusAllStops, TrafficSignals, BusPassengerStops, DisturbanceStops
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

        print(self.request.query_params)

        start_month = self.request.query_params.get("start_month", None)
        end_month = self.request.query_params.get("end_month", None)
        year = self.request.query_params.get("year", None)
        lines = self.request.query_params.get("lines", None)
        direction = self.request.query_params.get("direction", None)
        start_quarter_hour = self.request.query_params.get("start_quarter_hour", None)
        end_quarter_hour = self.request.query_params.get("end_quarter_hour", None)

        try:
            time_range = [int(start_quarter_hour), int(end_quarter_hour)]
            month_range = [int(start_month), int(end_month)]

            queryset = queryset.filter(
                opd_date__month__range=month_range,
                opd_date__year=int(year),
                pattern_direction=direction,
                start_quarter_hour__range=time_range,
                end_quarter_hour__range=time_range,
            )
        except TypeError:
            pass

        """
            line_id__in=[int(l) for l in lines.split(",")],

        """
        # queryset = queryset.filter(
        #     opd_date__month__gte=int(start_month),
        #     opd_date__month__lte=int(end_month),
        #     opd_date__year=int(year),
        #     line_id__in=[int(l) for l in lines.split(",")],
        #     pattern_direction=direction,
        #     start_quarter_hour__gte=int(start_quarter_hour),
        #     end_quarter_hour__lte=int(end_quarter_hour),
        # )

        # queryset = queryset.filter(
        #     opd_date__month__gte=int(start_month),
        #     opd_date__month__lte=int(end_month),
        #     opd_date__year=int(year),
        # )

        # queryset = queryset.filter(
        #     line_id__in=[int(l) for l in lines.split(",")],
        #     pattern_direction=direction,
        #     start_quarter_hour__gte=int(start_quarter_hour),
        #     end_quarter_hour__lte=int(end_quarter_hour),
        # )

        # start_month = self.request.query_params.get("start_month", None)
        # if start_month is not None:
        #     queryset = queryset.filter(opd_date__month__gte=int(start_month))

        # end_month = self.request.query_params.get("end_month", None)
        # if end_month is not None:
        #     queryset = queryset.filter(opd_date__month__lte=int(end_month))

        # lines = self.request.query_params.get("lines", None)
        # if lines is not None:
        #     queryset = queryset.filter(line_id__in=[int(l) for l in lines.split(",")])

        # direction = self.request.query_params.get("direction", None)
        # if direction is not None:
        #     queryset = queryset.filter(pattern_direction="I")

        # start_quarter_hour = self.request.query_params.get("start_quarter_hour", None)
        # if start_quarter_hour is not None:
        #     queryset = queryset.filter(start_quarter_hour__gte=int(start_quarter_hour))

        # end_quarter_hour = self.request.query_params.get("end_quarter_hour", None)
        # if end_quarter_hour is not None:
        #     queryset = queryset.filter(end_quarter_hour__lte=int(end_quarter_hour))

        # start_quarter_hour = self.request.query_params.get("start_quarter_hour", None)
        # end_quarter_hour = self.request.query_params.get("end_quarter_hour", None)
        # if start_quarter_hour is not None and end_quarter_hour is not None:
        #     _range = [start_quarter_hour, end_quarter_hour]
        #     queryset = queryset.filter(
        #         start_quarter_hour__in=_range, end_quarter_hour__in=_range
        #     )

        # num_results = self.request.query_params.get("num", None)
        # if num_results is not None:
        #     queryset = queryset[: int(num_results)]

        return queryset


class TrafficSignalsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of all the traffic signals in the Portland area.
    """

    queryset = TrafficSignals.objects.all()
    serializer_class = TrafficSignalsSerializer
