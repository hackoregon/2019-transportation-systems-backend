from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from toad.models import (
    BusAmRushSummary,
    BusPmRushSummary,
    BusPassengerStops,
    BusPassengerStopsCatalog,
    BusByStopSummary,
    BusSystemWideSummary,
    RailPassengerStops,
    RailPassengerStopsCatalog,
    RailAmRushSummary,
    RailPmRushSummary,
    RailByStopSummary,
    DisturbanceStops,
    DisturbanceStopsCatalog,
    DisturbanceSystemWideSummary,
    TrafficSignals,
    TmRailStops,
    TmRouteStops,
    RailSystemWideSummary,
    PassengerStopLocations,
    BusstopCatchmentZoneWithCensusAttribs
)

from toad.pre_existing_models import NcdbSampleTransportationCommute

from toad.serializers import (
    BusAmRushSummarySerializer,
    BusPmRushSummarySerializer,
    BusPassengerStopsSerializer,
    BusPassengerStopsCatalogSerializer,
    BusSystemWideSummarySerializer,
    BusByStopSummarySerializer,
    RailPassengerStopsSerializer,
    RailPassengerStopsCatalogSerializer,
    RailAmRushSummarySerializer,
    RailPmRushSummarySerializer,
    RailByStopSummarySerializer,
    DisturbanceStopsSerializer,
    DisturbanceStopsCatalogSerializer,
    DisturbanceSystemWideSummarySerializer,
    TrafficSignalsSerializer,
    TmRailStopsSerializer,
    TmRouteStopsSerializer,
    RailSystemWideSummarySerializer,
    PassengerStopLocationsSerializer,
    NcdbSampleTransportationCommuteSerializer,
    BusstopCatchmentZoneWithCensusAttribsSerializer
)

from toad.filters import (
    BusPassengerStopsFilter,
    RailPassengerStopsFilter,
    DisturbanceStopsFilter,
    BusAmRushSummaryFilter,
    BusPmRushSummaryFilter,
    BusByStopSummaryFilter,
    RailAmRushSummaryFilter,
    RailPmRushSummaryFilter,
    RailByStopSummaryFilter,
    BusstopCatchmentZoneWithCensusAttribsFilter
)


class BusAmRushSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Bus AM rush hour summary statistics.
    """

    serializer_class = BusAmRushSummarySerializer
    filter_backends = (BusAmRushSummaryFilter,)

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

        queryset = BusAmRushSummary.objects.filter(**filters)

        return queryset


class BusPmRushSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Bus PM rush hour summary statistics.
    """

    serializer_class = BusPmRushSummarySerializer
    filter_backends = (BusPmRushSummaryFilter,)

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

        queryset = BusPmRushSummary.objects.filter(**filters)

        return queryset


class BusSystemWideSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Bus System Wide summary statistics.
    """

    queryset = BusSystemWideSummary.objects.all()
    serializer_class = BusSystemWideSummarySerializer


class BusstopCatchmentZoneWithCensusAttribsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON shape of Bus Stop Catchment Zones.
    """

    serializer_class = BusstopCatchmentZoneWithCensusAttribsSerializer
    filter_backends = (BusstopCatchmentZoneWithCensusAttribsFilter,)

    def get_queryset(self):
        """
        Filters against query parameters in the URL.
        """

        filters = {}
        # really could use the assignment operator here :)

        lines = self.request.query_params.get("lines", False)
        if lines:
            try:
                filters["rte__in"] = [int(l) for l in lines.split(",")]
            except ValueError:
                raise ValidationError(
                    {"route_number": f"'{lines}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"route_number": f"'{lines}' - unknown error."})
        directions = self.request.query_params.get("directions", False)
        if directions:
            try:
                filters["dir__in"] = [int(d) for d in directions.split(",")]
            except ValueError:
                raise ValidationError(
                    {"dir": f"'{directions}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"dir": f"'{directions}' - unknown error."})
        stops = self.request.query_params.get("stops", False)
        if stops:
            try:
                filters["stop_id__in"] = [int(s) for s in stops.split(",")]
            except ValueError:
                raise ValidationError(
                    {"stop_id": f"'{stops}' is an invalid format."}
                )
            except Exception:
                raise ValidationError({"stop_id": f"'{stops}' - unknown error."})

        queryset = BusstopCatchmentZoneWithCensusAttribs.objects.filter(**filters)

        return queryset


class BusByStopSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Bus By Stop summary statistics.
    """

    serializer_class = BusByStopSummarySerializer
    filter_backends = (BusByStopSummaryFilter,)

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

        queryset = BusByStopSummary.objects.filter(**filters)

        return queryset


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


class BusPassengerStopsCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns a listing of the available year / month / route combinations
    with the number of rows in the table for Bus Passenger Stops
    """

    queryset = BusPassengerStopsCatalog.objects.all()
    serializer_class = BusPassengerStopsCatalogSerializer


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


class RailPassengerStopsCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns a listing of the available year / month / route combinations
    with the number of rows in the table for Rail Passenger Stops
    """

    queryset = RailPassengerStopsCatalog.objects.all()
    serializer_class = RailPassengerStopsCatalogSerializer


class RailAmRushSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Rail AM rush hour summary statistics.
    """

    serializer_class = RailAmRushSummarySerializer
    filter_backends = (RailAmRushSummaryFilter,)

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

        queryset = RailAmRushSummary.objects.filter(**filters)

        return queryset


class RailPmRushSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Rail PM rush hour summary statistics.
    """

    serializer_class = RailPmRushSummarySerializer
    filter_backends = (RailPmRushSummaryFilter,)

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

        queryset = RailPmRushSummary.objects.filter(**filters)

        return queryset


class RailByStopSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Rail By Stop summary statistics.
    """

    serializer_class = RailByStopSummarySerializer
    filter_backends = (RailByStopSummaryFilter,)

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

        queryset = RailByStopSummary.objects.filter(**filters)

        return queryset


class RailSystemWideSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns GeoJSON points of Rail System Wide summary statistics.
    """

    queryset = RailSystemWideSummary.objects.all()
    serializer_class = RailSystemWideSummarySerializer


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

        queryset = DisturbanceStops.objects.filter(**filters)

        return queryset


class DisturbanceStopsCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns a listing of the available year / month / route combinations
    with the number of rows in the table for Disturbance Stops
    """

    queryset = DisturbanceStopsCatalog.objects.all()
    serializer_class = DisturbanceStopsCatalogSerializer


class DisturbanceSystemWideSummaryViewSet(viewsets.ReadOnlyModelViewSet):
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


class PassengerStopLocationsViewSet(viewsets.ReadOnlyModelViewSet):
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
    filterset_fields = ('opp_zone', )
