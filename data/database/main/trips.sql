CREATE TABLE IF NOT EXISTS melbournetransit.trips (
    transport_type TEXT,
    route_id TEXT,
    service_id TEXT,
    trip_id TEXT,
    shape_id TEXT,
    trip_headsign TEXT,
    direction_id TEXT,
    block_id TEXT,
    wheelchair_accessible TEXT,
    bikes_allowed TEXT,
    PRIMARY KEY (transport_type, trip_id),
    FOREIGN KEY (transport_type, route_id) REFERENCES melbournetransit.routes(transport_type, route_id),
    FOREIGN KEY (transport_type, service_id) REFERENCES melbournetransit.calendar(transport_type, service_id)
);