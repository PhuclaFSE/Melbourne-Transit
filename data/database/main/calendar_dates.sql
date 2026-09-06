CREATE TABLE IF NOT EXISTS melbournetransit.calendar_dates (
    transport_type TEXT,
    service_id TEXT,
    date TEXT,
    exception_type TEXT,
    PRIMARY KEY (transport_type, service_id, date),
    FOREIGN KEY (transport_type, service_id) REFERENCES melbournetransit.calendar (transport_type, service_id)
);