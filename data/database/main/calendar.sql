CREATE TABLE IF NOT EXISTS melbournetransit.calendar (
    transport_type TEXT, 
    service_id TEXT,
    monday TEXT,
    tuesday TEXT,
    wednesday TEXT,
    thursday TEXT,
    friday TEXT,
    saturday TEXT,
    sunday TEXT,
    start_date TEXT,
    end_date TEXT,
    PRIMARY KEY (transport_type, service_id)
);