# MelbourneTransit — GTFS Data Engineering Pipeline

MelbourneTransit is a data engineering project focused on processing Victoria's public transport timetable data into a structured, queryable PostgreSQL/PostGIS database.

The project focuses on building a reproducible **extract, transform, and load (ETL) pipeline** for GTFS data rather than a web application. Its goal is to turn raw transport files into reliable relational datasets suitable for SQL analysis and spatial queries.

> **Project status:** Early development. The Docker-based PostgreSQL/PostGIS environment is in place. GTFS ingestion, validation, and loading workflows are planned and are not yet presented as implemented.

## Project Goals

- Ingest GTFS data for Victoria's train, tram, and bus services.
- Validate and transform raw timetable data before loading it.
- Model routes, stops, trips, schedules, and service calendars in PostgreSQL.
- Use PostGIS to support spatially aware transport analysis.
- Build a repeatable pipeline that can refresh datasets and report data-quality issues.

## Pipeline Architecture

```text
Victoria GTFS Datasets
        |
        v
Extract (Python)
        |
        v
Validate & Transform
        |
        v
Load (PostgreSQL + PostGIS)
        |
        v
SQL Quality Checks & Spatial Analysis
```

The architecture represents the intended pipeline. Only the local database environment is currently set up.

## Tech Stack

| Technology              | Role                                    | Status                |
| ----------------------- | --------------------------------------- | --------------------- |
| PostgreSQL 17           | Relational database                     | Set up                |
| PostGIS 3.5             | Spatial database extension              | Set up                |
| Docker / Docker Compose | Reproducible local database environment | Set up                |
| Python                  | GTFS extraction and transformation      | Planned               |
| SQL                     | Schema design, checks, and analysis     | In progress / planned |
| GTFS                    | Public transport source data            | Data model identified |

## GTFS Data Model

The pipeline is designed around the following GTFS files:

| Dataset          | Purpose                                                 |
| ---------------- | ------------------------------------------------------- |
| `routes`         | Transport routes and service types                      |
| `stops`          | Stop locations and identifiers                          |
| `trips`          | Individual journeys associated with routes and services |
| `stop_times`     | Scheduled arrival and departure times                   |
| `calendar`       | Recurring service schedules                             |
| `calendar_dates` | Exceptions to regular service schedules                 |

Additional GTFS files may be incorporated as the pipeline develops.

## Repository Structure

Current repository layout:

```text
Melbourne-Transit/
├── data/
│   └── database/
├── .gitignore
├── docker-compose.yml
└── README.md
```

ETL scripts, SQL definitions, and tests will be added as they are implemented. Raw GTFS datasets and local database files should generally remain outside version control.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Start PostgreSQL/PostGIS

```bash
git clone https://github.com/PhuclaFSE/Melbourne-Transit.git
cd Melbourne-Transit
docker compose up -d
```

The local development database uses:

| Setting    | Value        |
| ---------- | ------------ |
| PostgreSQL | 17           |
| PostGIS    | 3.5          |
| Database   | `meltransit` |
| User       | `postgres`   |
| Host       | `localhost`  |
| Port       | `5432`       |

Database storage uses a Docker volume to retain data across container restarts. Check `docker-compose.yml` for the actual database credentials and configuration before connecting.

Stop the containers:

```bash
docker compose down
```

## License

No license has been specified for this repository.

**La Gia Phuc**  
Bachelor of Computer Science — La Trobe University
