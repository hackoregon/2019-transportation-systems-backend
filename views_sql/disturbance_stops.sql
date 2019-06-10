DROP INDEX IF EXISTS bus_trips_event_no_trip_idx;
CREATE INDEX bus_trips_event_no_trip_idx ON bus_trips (event_no_trip);
DROP INDEX IF EXISTS bus_all_stops_event_no_trip_idx;
CREATE INDEX bus_all_stops_event_no_trip_idx ON bus_all_stops (event_no_trip);
DROP TABLE IF EXISTS disturbance_stops CASCADE;
CREATE TABLE disturbance_stops
AS
SELECT bus_all_stops.opd_date, date_part('dow', bus_all_stops.opd_date) AS day_of_week,
  bus_all_stops.act_arr_time, bus_all_stops.act_dep_time,
  0.25 * trunc(4 * date_part('hour', bus_all_stops.act_arr_time) +
    date_part('minute', bus_all_stops.act_arr_time) / 15) AS start_quarter_hour,
  0.25 * trunc(4 * date_part('hour', bus_all_stops.act_dep_time) +
    date_part('minute', bus_all_stops.act_dep_time) / 15) AS end_quarter_hour,
  bus_all_stops.act_dep_time - bus_all_stops.act_arr_time AS duration,
  bus_trips.line_id, bus_trips.pattern_direction,
  ST_X(geom_point_4326) AS longitude, ST_Y(geom_point_4326) AS latitude, geom_point_4326,
  bus_all_stops.id
FROM bus_all_stops
INNER JOIN bus_trips ON bus_trips.event_no_trip = bus_all_stops.event_no_trip
WHERE stop_type = 3;
ALTER TABLE disturbance_stops ADD PRIMARY KEY (id);
ALTER TABLE disturbance_stops
    OWNER TO transportation2019;
