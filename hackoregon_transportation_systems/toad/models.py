# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class BusByStopSummary(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.GeometryField(srid=0, blank=True, null=True)
    arrive_quarter_hour = models.FloatField(blank=True, null=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_seconds_late = models.FloatField(blank=True, null=True)
    q1_seconds_late = models.FloatField(blank=True, null=True)
    median_seconds_late = models.FloatField(blank=True, null=True)
    q3_seconds_late = models.FloatField(blank=True, null=True)
    p95_seconds_late = models.FloatField(blank=True, null=True)
    iqr_seconds_late = models.FloatField(blank=True, null=True)
    monthly_total_ons = models.BigIntegerField(blank=True, null=True)
    monthly_total_offs = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bus_by_stop_summary'


class BusPassengerStops(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    train = models.IntegerField(blank=True, null=True)
    trip_number = models.IntegerField(blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    arrive_time = models.DateTimeField(blank=True, null=True)
    leave_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    dwell = models.IntegerField(blank=True, null=True)
    door = models.IntegerField(blank=True, null=True)
    lift = models.IntegerField(blank=True, null=True)
    ons = models.IntegerField(blank=True, null=True)
    offs = models.IntegerField(blank=True, null=True)
    estimated_load = models.IntegerField(blank=True, null=True)
    train_mileage = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.PointField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    day_of_week = models.IntegerField(blank=True, null=True)
    seconds_late = models.IntegerField(blank=True, null=True)
    arriving_load = models.IntegerField(blank=True, null=True)
    arrive_quarter_hour = models.FloatField(blank=True, null=True)
    previous_location_id = models.IntegerField(blank=True, null=True)
    previous_arrive_time = models.DateTimeField(blank=True, null=True)
    previous_train_mileage = models.FloatField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bus_passenger_stops'
        unique_together = (('service_date', 'id'),)


class BusAmRushSummary(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.GeometryField(srid=0, blank=True, null=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_seconds_late = models.FloatField(blank=True, null=True)
    q1_seconds_late = models.FloatField(blank=True, null=True)
    median_seconds_late = models.FloatField(blank=True, null=True)
    q3_seconds_late = models.FloatField(blank=True, null=True)
    p95_seconds_late = models.FloatField(blank=True, null=True)
    iqr_seconds_late = models.FloatField(blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)
    total_offs = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bus_am_rush_summary'


class BusPmRushSummary(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.GeometryField(srid=0, blank=True, null=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_seconds_late = models.FloatField(blank=True, null=True)
    q1_seconds_late = models.FloatField(blank=True, null=True)
    median_seconds_late = models.FloatField(blank=True, null=True)
    q3_seconds_late = models.FloatField(blank=True, null=True)
    p95_seconds_late = models.FloatField(blank=True, null=True)
    iqr_seconds_late = models.FloatField(blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)
    total_offs = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bus_pm_rush_summary'


class BusRoutes(models.Model):
    line_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bus_routes'


class BusServiceKeys(models.Model):
    service_date = models.DateField(primary_key=True)
    service_key = models.TextField()

    class Meta:
        managed = False
        db_table = 'bus_service_keys'
        unique_together = (('service_date', 'service_key'),)


class BusSystemWideSummary(models.Model):
    arrive_quarter_hour = models.FloatField(primary_key=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_seconds_late = models.FloatField(blank=True, null=True)
    q1_seconds_late = models.FloatField(blank=True, null=True)
    median_seconds_late = models.FloatField(blank=True, null=True)
    q3_seconds_late = models.FloatField(blank=True, null=True)
    p95_seconds_late = models.FloatField(blank=True, null=True)
    iqr_seconds_late = models.FloatField(blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)
    total_offs = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_system_wide_summary'


class BusTrips(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    opd_date = models.DateField(blank=True, null=True)
    act_dep_time = models.DateTimeField(blank=True, null=True)
    act_end_time = models.DateTimeField(blank=True, null=True)
    nom_dep_time = models.DateTimeField(blank=True, null=True)
    nom_end_time = models.DateTimeField(blank=True, null=True)
    event_no_trip = models.IntegerField(blank=True, null=True)
    meters = models.IntegerField(blank=True, null=True)
    line_id = models.IntegerField(blank=True, null=True)
    pattern_direction = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "bus_trips"


class CurrentStopLocations(models.Model):
    stop_id = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_stop_locations'


class DisturbanceStops(models.Model):
    opd_date = models.DateField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    day_of_week = models.IntegerField(blank=True, null=True)
    act_arr_time = models.DateTimeField(blank=True, null=True)
    act_dep_time = models.DateTimeField(blank=True, null=True)
    start_quarter_hour = models.FloatField(blank=True, null=True)
    end_quarter_hour = models.FloatField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    line_id = models.IntegerField(blank=True, null=True)
    pattern_direction = models.TextField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.PointField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "disturbance_stops"
        unique_together = (("opd_date", "id"),)


class DisturbanceSystemWideSummary(models.Model):
    start_quarter_hour = models.FloatField(primary_key=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_duration = models.FloatField(blank=True, null=True)
    q1_duration = models.FloatField(blank=True, null=True)
    median_duration = models.FloatField(blank=True, null=True)
    q3_duration = models.FloatField(blank=True, null=True)
    p95_duration = models.FloatField(blank=True, null=True)
    iqr_duration = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disturbance_system_wide_summary'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class HealthCheckDbTestmodel(models.Model):
    title = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'health_check_db_testmodel'


class PassengerCensus(models.Model):
    summary_begin_date = models.DateField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    stop_seq = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    public_location_description = models.TextField(blank=True, null=True)
    ons = models.IntegerField(blank=True, null=True)
    offs = models.IntegerField(blank=True, null=True)
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'passenger_census'


class PassengerStopLocations(models.Model):
    stop_id = models.IntegerField(primary_key=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger_stop_locations'


class RailAmRushSummary(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.GeometryField(srid=0, blank=True, null=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_seconds_late = models.FloatField(blank=True, null=True)
    q1_seconds_late = models.FloatField(blank=True, null=True)
    median_seconds_late = models.FloatField(blank=True, null=True)
    q3_seconds_late = models.FloatField(blank=True, null=True)
    p95_seconds_late = models.FloatField(blank=True, null=True)
    iqr_seconds_late = models.FloatField(blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)
    total_offs = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rail_am_rush_summary'


class RailByStopSummary(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.GeometryField(srid=0, blank=True, null=True)
    arrive_quarter_hour = models.FloatField(blank=True, null=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_seconds_late = models.FloatField(blank=True, null=True)
    q1_seconds_late = models.FloatField(blank=True, null=True)
    median_seconds_late = models.FloatField(blank=True, null=True)
    q3_seconds_late = models.FloatField(blank=True, null=True)
    p95_seconds_late = models.FloatField(blank=True, null=True)
    iqr_seconds_late = models.FloatField(blank=True, null=True)
    monthly_total_ons = models.BigIntegerField(blank=True, null=True)
    monthly_total_offs = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rail_by_stop_summary'


class RailPassengerStops(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    arrive_time = models.DateTimeField(blank=True, null=True)
    leave_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    dwell = models.IntegerField(blank=True, null=True)
    door = models.IntegerField(blank=True, null=True)
    lift = models.IntegerField(blank=True, null=True)
    ons = models.IntegerField(blank=True, null=True)
    offs = models.IntegerField(blank=True, null=True)
    estimated_load = models.IntegerField(blank=True, null=True)
    train_mileage = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.PointField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    seconds_late = models.IntegerField(blank=True, null=True)
    arriving_load = models.IntegerField(blank=True, null=True)
    arrive_quarter_hour = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "rail_passenger_stops"
        unique_together = (("service_date", "id"),)


class RailPmRushSummary(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.GeometryField(srid=0, blank=True, null=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_seconds_late = models.FloatField(blank=True, null=True)
    q1_seconds_late = models.FloatField(blank=True, null=True)
    median_seconds_late = models.FloatField(blank=True, null=True)
    q3_seconds_late = models.FloatField(blank=True, null=True)
    p95_seconds_late = models.FloatField(blank=True, null=True)
    iqr_seconds_late = models.FloatField(blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)
    total_offs = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rail_pm_rush_summary'


class RailSystemWideSummary(models.Model):
    arrive_quarter_hour = models.FloatField(primary_key=True)
    samples = models.BigIntegerField(blank=True, null=True)
    p05_seconds_late = models.FloatField(blank=True, null=True)
    q1_seconds_late = models.FloatField(blank=True, null=True)
    median_seconds_late = models.FloatField(blank=True, null=True)
    q3_seconds_late = models.FloatField(blank=True, null=True)
    p95_seconds_late = models.FloatField(blank=True, null=True)
    iqr_seconds_late = models.FloatField(blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)
    total_offs = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rail_system_wide_summary'


class TmRailStops(models.Model):
    # inspectdb returns maxlength of -1, setting to 255 for now
    ogc_fid = models.AutoField(primary_key=True)
    station = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    line = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tm_rail_stops"


class TmRouteStops(models.Model):
    # inspectdb returns maxlength of -1, setting to 255 for now
    ogc_fid = models.AutoField(primary_key=True)
    rte = models.IntegerField(blank=True, null=True)
    dir = models.IntegerField(blank=True, null=True)
    rte_desc = models.CharField(max_length=255, blank=True, null=True)
    dir_desc = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    stop_seq = models.IntegerField(blank=True, null=True)
    stop_id = models.IntegerField(blank=True, null=True)
    stop_name = models.CharField(max_length=255, blank=True, null=True)
    jurisdic = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    frequent = models.CharField(max_length=255, blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tm_route_stops"


class TrafficSignals(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    assetid = models.CharField(max_length=80, blank=True, null=True)
    owner = models.CharField(max_length=80, blank=True, null=True)
    maintresp = models.CharField(max_length=80, blank=True, null=True)
    locationid = models.CharField(max_length=80, blank=True, null=True)
    imagepath = models.CharField(max_length=120, blank=True, null=True)
    powersuppl = models.CharField(max_length=80, blank=True, null=True)
    ismetered = models.CharField(max_length=80, blank=True, null=True)
    engineer = models.CharField(max_length=80, blank=True, null=True)
    electricia = models.CharField(max_length=80, blank=True, null=True)
    signalnum = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    signaltype = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    actuation = models.CharField(max_length=80, blank=True, null=True)
    roadauthor = models.CharField(max_length=80, blank=True, null=True)
    signalsyst = models.CharField(max_length=80, blank=True, null=True)
    primarycon = models.CharField(max_length=80, blank=True, null=True)
    hubloc = models.CharField(max_length=80, blank=True, null=True)
    commsource = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    masterloc = models.CharField(max_length=80, blank=True, null=True)
    emergencyp = models.CharField(max_length=80, blank=True, null=True)
    railroadpe = models.CharField(max_length=80, blank=True, null=True)
    buspe = models.CharField(max_length=80, blank=True, null=True)
    lightrailp = models.CharField(max_length=80, blank=True, null=True)
    otherpe = models.CharField(max_length=80, blank=True, null=True)
    controller = models.CharField(max_length=80, blank=True, null=True)
    cabinettyp = models.CharField(max_length=80, blank=True, null=True)
    cabinetcha = models.CharField(max_length=80, blank=True, null=True)
    controll_1 = models.CharField(max_length=80, blank=True, null=True)
    softwarety = models.CharField(max_length=80, blank=True, null=True)
    softwarere = models.CharField(max_length=80, blank=True, null=True)
    temptiming = models.CharField(max_length=80, blank=True, null=True)
    servicevol = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    lastremode = models.CharField(max_length=80, blank=True, null=True)
    standardsc = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    wkb_geometry = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "traffic_signals"
