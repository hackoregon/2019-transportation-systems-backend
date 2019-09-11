import coreapi
from django_filters.rest_framework import DjangoFilterBackend
from toad.models import (
    BusPassengerStops,
    DisturbanceStops,
    RailPassengerStops,
    BusAmRushSummary,
    BusPmRushSummary,
    BusByStopSummary,
    RailAmRushSummary,
    RailPmRushSummary,
    RailByStopSummary,
    BusstopCatchmentZoneWithCensusAttribs,
    RidershipDemographics
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
                name="years",
                required=True,
                location="query",
                type="string",
                description="Years to filter on. Example: '2017' or '2017,2018'.",
            ),
            coreapi.Field(
                name="months",
                required=True,
                location="query",
                type="string",
                description="Months to filter on (integer). Example: '9,10' to include September and October.",
            ),
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


class RailPassengerStopsFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = RailPassengerStops

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="years",
                required=True,
                location="query",
                type="string",
                description="Years to filter on. Example: '2017' or '2017,2018'.",
            ),
            coreapi.Field(
                name="months",
                required=True,
                location="query",
                type="string",
                description="Months to filter on (integer). Example: '9,10' to include September and October.",
            ),
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
        ]
        return fields


class BusAmRushSummaryFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = BusAmRushSummary

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="bounds",
                required=False,
                location="query",
                type="string",
                description="Four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). Example: -122.665849,45.510867,-122.653650,45.514367",
            ),
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Bus routes to include. Example: '10,14' for routes 10 and 14.",
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


class BusPmRushSummaryFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = BusPmRushSummary

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="bounds",
                required=False,
                location="query",
                type="string",
                description="Four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). Example: -122.665849,45.510867,-122.653650,45.514367",
            ),
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Bus routes to include. Example: '10,14' for routes 10 and 14.",
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


class BusByStopSummaryFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = BusByStopSummary

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="bounds",
                required=False,
                location="query",
                type="string",
                description="Four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). Example: -122.665849,45.510867,-122.653650,45.514367",
            ),
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Bus routes to include. Example: '10,14' for routes 10 and 14.",
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


class RailAmRushSummaryFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = RailAmRushSummary

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="bounds",
                required=False,
                location="query",
                type="string",
                description="Four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). Example: -122.665849,45.510867,-122.653650,45.514367",
            ),
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Rail routes to include. `90` - RED, `100` - BLUE, `190` - YELLOW, `200` - GREEN, `290` - ORANGE. Example: '90,100' for the RED and BLUE lines.",
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


class RailPmRushSummaryFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = RailPmRushSummary

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="bounds",
                required=False,
                location="query",
                type="string",
                description="Four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). Example: -122.665849,45.510867,-122.653650,45.514367",
            ),
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Rail routes to include. `90` - RED, `100` - BLUE, `190` - YELLOW, `200` - GREEN, `290` - ORANGE. Example: '90,100' for the RED and BLUE lines.",
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


class RailByStopSummaryFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = RailByStopSummary

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="bounds",
                required=False,
                location="query",
                type="string",
                description="Four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). Example: -122.665849,45.510867,-122.653650,45.514367",
            ),
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Rail routes to include. `90` - RED, `100` - BLUE, `190` - YELLOW, `200` - GREEN, `290` - ORANGE. Example: '90,100' for the RED and BLUE lines.",
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


class BusstopCatchmentZoneWithCensusAttribsFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = BusstopCatchmentZoneWithCensusAttribs

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Bus/Rail routes to include. `90` - RED, `100` - BLUE, `190` - YELLOW, `200` - GREEN, `290` - ORANGE. Example: '90,100' for the RED and BLUE lines.",
            ),
            coreapi.Field(
                name="directions",
                required=False,
                location="query",
                type="string",
                description="Line direction\n\n1 for Inbound (or often Southbound)\n0 for Outbound (or often Northbound)\n\nExample:\t1,0\n\nReturns data from both directions of a route.",
            ),
            coreapi.Field(
                name="stops",
                required=False,
                location="query",
                type="string",
                description="Stop ids to include, separated by a comma.\n\nExample:\tstopid1,stopid2,stopid3\n\nReturns data for only these stops.",
            ),
        ]

        return fields


class RidershipDemographicsFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into the schema.
    """

    class Meta:
        model = RidershipDemographics

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name="lines",
                required=False,
                location="query",
                type="string",
                description="Bus/Rail routes to include. `90` - RED, `100` - BLUE, `190` - YELLOW, `200` - GREEN. Example: '90,100' for the RED and BLUE lines.",
            ),
            coreapi.Field(
                name="directions",
                required=False,
                location="query",
                type="string",
                description="Line direction\n\n1 for Inbound (or often Southbound)\n0 for Outbound (or often Northbound)\n\nExample:\t1,0\n\nReturns data from both directions of a route.",
            ),
            coreapi.Field(
                name="stops",
                required=False,
                location="query",
                type="string",
                description="Stop ids to include, separated by a comma.\n\nExample:\tstopid1,stopid2,stopid3\n\nReturns data for only these stops.",
            ),
        ]

        return fields
