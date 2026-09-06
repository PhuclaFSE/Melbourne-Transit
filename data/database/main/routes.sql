CREATE TABLE IF NOT EXISTS melbournetransit.routes (
    transport_type TEXT,
    route_id TEXT,
    agency_id TEXT,
    route_short_name TEXT,
    route_long_name TEXT,
    route_type TEXT,
    route_color TEXT,
    route_text_color TEXT,
    PRIMARY KEY (transport_type, route_id)
);