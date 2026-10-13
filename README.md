# MelbourneTransit

MelbourneTransit is a full-stack public transport project for exploring Melbourne's train, tram, and bus network.

The project is being built around Victoria's GTFS public transport data, with PostgreSQL/PostGIS as the data layer. The long-term goal is to develop the system from raw transport data through to a web application with route exploration, mapping, and eventually an independent journey-planning engine.

> **Project status:** Early development. The current repository focuses on the database and data setup. Backend and frontend components will be added progressively.

## Current Progress

Currently implemented:

- PostgreSQL database environment
- PostGIS support for future geospatial queries
- Docker-based local database setup
- Initial public transport data/database structure
- Local development configuration through Docker Compose

The current Docker environment runs:

- PostgreSQL 17
- PostGIS 3.5
- Database: `meltransit`
- Local PostgreSQL port: `5432`

## Planned Architecture

MelbourneTransit is planned as an end-to-end transport system:

```text
GTFS Data
    |
    v
Data Processing / ETL
    |
    v
PostgreSQL + PostGIS
    |
    v
Node.js + Express REST API
    |
    v
React Frontend
    |
    v
Leaflet Map
```

The project is being developed incrementally, starting from the transport data layer before building the API and user interface.

## Tech Stack

### Currently Used

- PostgreSQL
- PostGIS
- Docker
- Docker Compose
- GTFS transport data

### Planned

- Python — GTFS data processing and loading
- Node.js
- Express.js
- REST APIs
- React
- JavaScript
- Tailwind CSS
- Leaflet

## Project Structure

Current repository structure:

```text
Melbourne-Transit/
│
├── data/
│   └── database/
│
├── .gitignore
├── docker-compose.yml
└── README.md
```

The structure will expand as the backend and frontend are added.

## Database Setup

The development database runs inside Docker using PostgreSQL with PostGIS.

### Requirements

Install:

- Docker
- Docker Compose

### Start the Database

Clone the repository:

```bash
git clone https://github.com/PhuclaFSE/Melbourne-Transit.git
cd Melbourne-Transit
```

Start PostgreSQL:

```bash
docker compose up -d
```

The database will be available locally on:

```text
localhost:5432
```

Current development configuration:

```text
Database: meltransit
User: postgres
Port: 5432
```

Database data is stored using a Docker volume so it can persist between container restarts.

To stop the container:

```bash
docker compose down
```

## GTFS Data

MelbourneTransit is designed around General Transit Feed Specification (GTFS) data for Victoria's public transport network.

The project will work with core GTFS datasets such as:

```text
routes
stops
trips
stop_times
calendar
calendar_dates
```

These datasets provide the foundation for representing transport routes, services, stops, trips, and timetables.

Raw GTFS data should remain outside version control where appropriate rather than being committed directly to the repository.

## Development Roadmap

### Phase 1 — Data Layer

- [x] Set up PostgreSQL
- [x] Enable PostGIS environment
- [x] Dockerise the development database
- [ ] Complete GTFS database schema
- [ ] Build GTFS loading pipeline
- [ ] Import train data
- [ ] Import tram data
- [ ] Import bus data
- [ ] Validate imported transport data

### Phase 2 — Backend

- [ ] Set up Node.js and Express
- [ ] Connect backend to PostgreSQL
- [ ] Build route API
- [ ] Build stop API
- [ ] Add route detail endpoints
- [ ] Add stop and timetable queries

### Phase 3 — Frontend

- [ ] Set up React frontend
- [ ] Browse train, tram, and bus routes
- [ ] Search routes and stops
- [ ] Display route details
- [ ] Integrate Leaflet maps
- [ ] Display stops and route shapes

### Phase 4 — Journey Planning

- [ ] Build journey search interface
- [ ] Implement nearby-stop search
- [ ] Implement RAPTOR routing algorithm
- [ ] Support transfers between services
- [ ] Display journey results on the map
- [ ] Add Free Tram Zone detection

## Journey Planning

A major future goal of MelbourneTransit is to build the journey-planning logic directly from GTFS data instead of relying on an external journey-planning service.

The planned flow is:

```text
Origin + Destination
        |
        v
Nearby Stops
        |
        v
RAPTOR Routing
        |
        v
Candidate Journeys
        |
        v
Journey Details
        |
        v
Map Visualisation
```

This part of the project will be developed after the core transport database, API, and route visualisation are working reliably.

## Why I Built This

I started MelbourneTransit to learn full-stack development using a real dataset and a system that is more complex than a standard CRUD application.

The project gives me a practical way to work with several areas of software engineering in the same system:

- relational databases
- spatial data
- data processing
- REST API design
- backend architecture
- frontend development
- mapping
- public transport data
- routing algorithms

The project will grow gradually from the database layer into a complete transport application, with the journey-planning engine being one of the later and more algorithmically challenging parts.

## Status

MelbourneTransit is actively under development.

The current focus is building and validating the transport data layer before moving on to the backend API.

## Author

**La Gia Phuc**

Bachelor of Computer Science  
La Trobe University
