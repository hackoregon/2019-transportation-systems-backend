SELECT bus_all_stops.opd_date, DATE_PART('dow', bus_all_stops.opd_date) AS day_of_week,
  bus_all_stops.act_arr_time, bus_all_stops.act_dep_time, 
  bus_all_stops.act_dep_time - bus_all_stops.act_arr_time AS duration,
  bus_trips.line_id, geom_point_4326
FROM bus_all_stops
LEFT JOIN bus_trips ON bus_trips.event_no_trip = bus_all_stops.event_no_trip
WHERE stop_type = 3
LIMIT 100;