CREATE TABLE IF NOT EXISTS temp.stops (
    stop_id TEXT,
    stop_code TEXT,
    stop_name TEXT,
    stop_lat DOUBLE PRECISION,
    stop_lon DOUBLE PRECISION, 
    stop_url TEXT,
    location_type TEXT,
    parent_station TEXT,
    wheelchair_boarding TEXT,
    level_id TEXT,
    platform_code TEXT,
    geom GEOMETRY(POINT, 4326)
);