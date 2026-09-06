import os
import psycopg2
import csv
from dotenv import load_dotenv

load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
host = os.getenv("DB_HOST")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")

dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "gtfs")
transports = ["train", "tram", "bus"]


def copy_dynamic_header(cur, file_path, temp_table, allowed_columns):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        columns = next(reader)

        unexpected = set(columns) - allowed_columns

        if unexpected:
            raise ValueError(f"Unexpected columns in {file_path}: {unexpected}")

        column_sql = ", ".join(columns)

        f.seek(0)

        cur.copy_expert(
            f"""
            COPY {temp_table} ({column_sql})
            FROM STDIN
            WITH (FORMAT CSV, HEADER TRUE)
        """,
            f,
        )


try:
    conn = psycopg2.connect(
        dbname=dbname, user=user, host=host, password=password, port=port
    )
    with conn.cursor() as cur:
        print("[DB] Loading data...")
        cur.execute("""
                    TRUNCATE TABLE
                        melbournetransit.calendar,
                        melbournetransit.calendar_dates,
                        melbournetransit.stops,
                        melbournetransit.routes,
                        melbournetransit.trips,
                        melbournetransit.stop_times
                    CASCADE;
                    """)
        for transport in transports:
            print(f"\n[DB] {transport}")

            # ----- Calendar -----#

            print("[DB] Loading calendar...")
            calendar_sc = os.path.join(dir, transport, "calendar.txt")
            cur.execute("TRUNCATE TABLE temp.calendar")
            allowed_calendar_columns = {
                "service_id",
                "monday",
                "tuesday",
                "wednesday",
                "thursday",
                "friday",
                "saturday",
                "sunday",
                "start_date",
                "end_date",
            }

            copy_dynamic_header(
                cur, calendar_sc, "temp.calendar", allowed_calendar_columns
            )
            cur.execute(
                """
                    INSERT INTO melbournetransit.calendar (
                        transport_type,
                        service_id, 
                        monday, 
                        tuesday, 
                        wednesday, 
                        thursday, 
                        friday,
                        saturday, 
                        sunday, 
                        start_date, 
                        end_date
                    )
                    SELECT 
                        %s, 
                        service_id, 
                        monday, 
                        tuesday, 
                        wednesday, 
                        thursday, 
                        friday,
                        saturday, 
                        sunday, 
                        start_date, 
                        end_date
                    FROM temp.calendar
                """,
                (transport,),
            )
            print("[DB] Done!")

            # ----- Calendar_date -----#

            print("[DB] Loading calendar_dates...")
            calendar_date_sc = os.path.join(dir, transport, "calendar_dates.txt")
            cur.execute("TRUNCATE TABLE temp.calendar_dates")
            allowed_calendar_date_columns = {"service_id", "date", "exception_type"}

            copy_dynamic_header(
                cur,
                calendar_date_sc,
                "temp.calendar_dates",
                allowed_calendar_date_columns,
            )
            cur.execute(
                """
                    INSERT INTO melbournetransit.calendar_dates (
                        transport_type,
                        service_id, 
                        date, 
                        exception_type
                    )
                    SELECT 
                        %s, 
                        service_id,
                        date, 
                        exception_type
                    FROM temp.calendar_dates
                """,
                (transport,),
            )
            print("[DB] Done!")

            # ----- Stops -----#

            print("[DB] Loading stops...")
            stop_sc = os.path.join(dir, transport, "stops.txt")
            cur.execute("TRUNCATE TABLE temp.stops")
            allowed_stop_columns = {
                "stop_id",
                "stop_code",
                "stop_name",
                "stop_lat",
                "stop_lon",
                "stop_url",
                "location_type",
                "parent_station",
                "wheelchair_boarding",
                "level_id",
                "platform_code",
            }
            copy_dynamic_header(cur, stop_sc, "temp.stops", allowed_stop_columns)
            cur.execute(
                """
                INSERT INTO melbournetransit.stops (
                    transport_type,
                    stop_id,
                    stop_code,
                    stop_name,
                    stop_lat,
                    stop_lon,
                    stop_url,
                    location_type,
                    parent_station,
                    wheelchair_boarding,
                    level_id,
                    platform_code
                )
                SELECT
                    %s,
                    stop_id,
                    stop_code,
                    stop_name,
                    stop_lat,
                    stop_lon,
                    stop_url,
                    location_type,
                    parent_station,
                    wheelchair_boarding,
                    level_id,
                    platform_code
                FROM temp.stops
            """,
                (transport,),
            )

            print("[DB] Done!")

            # ----- Routes -----#

            print("[DB] Loading routes...")
            route_sc = os.path.join(dir, transport, "routes.txt")
            cur.execute("TRUNCATE TABLE temp.routes")
            allowed_route_columns = {
                "route_id",
                "agency_id",
                "route_short_name",
                "route_long_name",
                "route_type",
                "route_color",
                "route_text_color",
            }

            copy_dynamic_header(cur, route_sc, "temp.routes", allowed_route_columns)
            cur.execute(
                """
                    INSERT INTO melbournetransit.routes (
                        transport_type,
                        route_id,
                        agency_id,
                        route_short_name,
                        route_long_name,
                        route_type,
                        route_color,
                        route_text_color
                    )
                    SELECT 
                        %s, 
                        route_id,
                        agency_id,
                        route_short_name,
                        route_long_name,
                        route_type,
                        route_color,
                        route_text_color
                    FROM temp.routes
                """,
                (transport,),
            )
            print("[DB] Done!")

            # ----- Trips -----#

            print("[DB] Loading trips...")
            trip_sc = os.path.join(dir, transport, "trips.txt")
            cur.execute("TRUNCATE TABLE temp.trips")
            allowed_trip_columns = {
                "route_id",
                "service_id",
                "trip_id",
                "shape_id",
                "trip_headsign",
                "direction_id",
                "block_id",
                "wheelchair_accessible",
                "bikes_allowed",
            }

            copy_dynamic_header(cur, trip_sc, "temp.trips", allowed_trip_columns)
            cur.execute(
                """
                    INSERT INTO melbournetransit.trips (
                        transport_type, 
                        route_id,
                        service_id,
                        trip_id,
                        shape_id,
                        trip_headsign,
                        direction_id,
                        block_id,
                        wheelchair_accessible,
                        bikes_allowed
                    )
                    SELECT
                        %s, 
                        route_id,
                        service_id,
                        trip_id,
                        shape_id,
                        trip_headsign,
                        direction_id,
                        block_id,
                        wheelchair_accessible,
                        bikes_allowed
                    FROM temp.trips
                """,
                (transport,),
            )
            print("[DB] Done!")

            # ----- Stop_times -----#

            print("[DB] Loading stop_times...")
            stop_time_sc = os.path.join(dir, transport, "stop_times.txt")
            cur.execute("TRUNCATE TABLE temp.stop_times")
            allowed_stop_time_columns = {
                "trip_id",
                "arrival_time",
                "departure_time",
                "stop_id",
                "stop_sequence",
                "stop_headsign",
                "pickup_type",
                "drop_off_type",
                "shape_dist_traveled",
            }

            copy_dynamic_header(
                cur, stop_time_sc, "temp.stop_times", allowed_stop_time_columns
            )
            cur.execute(
                """
                    INSERT INTO melbournetransit.stop_times (
                        transport_type, 
                        trip_id,
                        arrival_time,
                        departure_time,
                        stop_id,
                        stop_sequence,
                        stop_headsign,
                        pickup_type,
                        drop_off_type,
                        shape_dist_traveled                        
                    )
                    SELECT 
                        %s,
                        trip_id,
                        arrival_time,
                        departure_time,
                        stop_id,
                        stop_sequence,
                        stop_headsign,
                        pickup_type,
                        drop_off_type,
                        shape_dist_traveled    
                    FROM temp.stop_times                    
                """,
                (transport,),
            )
            print("[DB] Done!")

        # ----- Update Geometry -----#

        print("\n[DB] Creating stop geometries...")
        cur.execute("""
            UPDATE melbournetransit.stops
            SET geom = ST_SetSRID(
                ST_MakePoint(stop_lon, stop_lat),
                4326
            )
            WHERE stop_lon IS NOT NULL
            AND stop_lat IS NOT NULL;
        """)

        # ----- Delete temp tables -----#

        print("[DB] Deleating temp...")
        cur.execute("DROP SCHEMA temp CASCADE")
        conn.commit()
        print("[DB] Data loaded successfully")
except Exception as e:
    print(f"[ERR] {e}")
    if "conn" in locals():
        conn.rollback()
finally:
    if "conn" in locals():
        conn.close()
