CREATE TABLE IF NOT EXISTS melbournetransit.stop_times (
    transport_type TEXT,
    trip_id TEXT,
    arrival_time TEXT,
    departure_time TEXT,
    stop_id TEXT,
    stop_sequence TEXT,
    stop_headsign TEXT,
    pickup_type TEXT,
    drop_off_type TEXT,
    shape_dist_traveled TEXT,
    PRIMARY KEY (transport_type, trip_id, stop_sequence),
    FOREIGN KEY (transport_type, trip_id) REFERENCES melbournetransit.trips (transport_type, trip_id),
    FOREIGN KEY (transport_type, stop_id) REFERENCES melbournetransit.stops (transport_type, stop_id)
);