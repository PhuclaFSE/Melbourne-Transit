# MelbourneTransit

MelbourneTransit is a full-stack public transport web application for exploring Melbourne's train, tram, and bus network.

The project uses Victorian public transport GTFS data, stores it in PostgreSQL/PostGIS, exposes the data through a Node.js/Express REST API, and displays transport information through a React frontend.

The long-term goal is to build a complete journey-planning system with my own routing implementation instead of relying on external journey-planning APIs.

## Features

### Current

- Browse Melbourne train, tram, and bus routes
- Filter routes by transport mode
- Search and retrieve transport data through a REST API
- Store GTFS transport data in PostgreSQL
- Process GTFS datasets using a Python ETL pipeline
- Separate backend logic into routes, controllers, and services
- Display transport information through a React frontend
- Support geographic transport data with PostGIS

### Planned

- Route detail pages
- Stop search and stop detail pages
- Interactive route maps using Leaflet
- Visualisation of route shapes and stops
- Journey planning between two locations
- Custom RAPTOR-based public transport routing algorithm
- Free Tram Zone detection and alerts
- Improved service and disruption information where suitable data is available

## Tech Stack

### Frontend

- React
- JavaScript
- Tailwind CSS
- shadcn/ui
- Leaflet

### Backend

- Node.js
- Express.js
- REST APIs

### Database

- PostgreSQL
- PostGIS

### Data Processing

- Python
- psycopg2
- GTFS

### Development Tools

- Git
- GitHub
- Docker

## Architecture

MelbourneTransit follows a simple full-stack architecture:

```text
GTFS Data
    |
    v
Python ETL Pipeline
    |
    v
PostgreSQL + PostGIS
    |
    v
Node.js / Express API
    |
    v
React Frontend
    |
    v
Leaflet Map
```

The backend is separated into layers to keep the code easier to maintain:

```text
Route
  |
  v
Controller
  |
  v
Service
  |
  v
PostgreSQL
```

For example, a request for train routes follows this flow:

```text
GET /api/routes?type=train
        |
        v
Express Router
        |
        v
Route Controller
        |
        v
Route Service
        |
        v
PostgreSQL
```

## Project Structure

```text
MelbourneTransit/
│
├── backend/
│   ├── controllers/
│   ├── routes/
│   ├── services/
│   ├── db.js
│   └── server.js
│
├── frontend/
│   ├── src/
│   │   ├── Components/
│   │   ├── pages/
│   │   └── assets/
│   └── package.json
│
├── database/
│   └── SQL scripts
│
├── data/
│   ├── Train/
│   ├── Tram/
│   └── Bus/
│
├── create_db.py
├── load_gtfs.py
└── README.md
```

> Raw GTFS datasets are not committed to this repository.

## GTFS Data

The application currently works with the main GTFS tables required for route and timetable information:

- `routes`
- `stops`
- `trips`
- `stop_times`
- `calendar`
- `calendar_dates`

The source datasets are separated into train, tram, and bus data before being loaded into PostgreSQL.

The ETL process handles the conversion from raw GTFS text files into relational database tables that can be queried by the backend.

## API

### Get Routes

```http
GET /api/routes?type=train
```

Supported transport types:

```text
train
tram
bus
```

Example:

```http
GET /api/routes?type=tram
```

The API validates the requested transport mode before querying the database.

Example response:

```json
[
  {
    "route_id": "...",
    "route_short_name": "86",
    "route_long_name": "...",
    "transport_type": "tram"
  }
]
```

## Database Querying

Database queries use parameterised SQL where user-controlled values are involved.

Example:

```sql
SELECT *
FROM melbournetransit.routes
WHERE transport_type = $1;
```

Different transport modes require different sorting behaviour.

For example:

- train routes are sorted by their route name
- tram routes are sorted numerically
- bus routes must support both numeric and named route identifiers

Replacement bus entries contained in the GTFS data are filtered from the normal train route list.

## Journey Planning

A major future part of MelbourneTransit is the journey-planning engine.

Instead of using Google Maps or another external journey-planning API, the project is intended to calculate journeys directly from GTFS data.

The planned routing pipeline is:

```text
Origin
   |
   v
Nearby Stops
   |
   v
RAPTOR Routing Algorithm
   |
   v
Candidate Journeys
   |
   v
Journey Details
   |
   v
Frontend Map
```

RAPTOR is designed specifically for public transport routing and works around rounds of route scanning rather than traditional road-network shortest-path traversal.

This part of the project is currently under development.

## Running the Project

### Requirements

Install:

- Node.js
- npm
- Python
- PostgreSQL
- PostGIS

### 1. Clone the repository

```bash
git clone <repository-url>
cd MelbourneTransit
```

### 2. Configure the database

Create a PostgreSQL database and enable PostGIS.

```sql
CREATE EXTENSION postgis;
```

Create a local `.env` file for backend configuration.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=melbournetransit
DB_USER=postgres
DB_PASSWORD=your_password
PORT=3000
```

Do not commit `.env` files or database credentials to GitHub.

### 3. Load GTFS data

Place the required GTFS datasets inside the local `data/` directory.

Then run the database setup and ETL scripts.

```bash
python create_db.py
python load_gtfs.py
```

### 4. Start the backend

```bash
cd backend
npm install
npm run dev
```

The API runs locally on:

```text
http://localhost:3000
```

### 5. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL shown by the frontend development server.

## Development Roadmap

```text
[x] GTFS data ingestion
[x] PostgreSQL database
[x] Basic route API
[x] Train, tram and bus filtering
[x] React route rendering

[ ] Route detail API
[ ] Stop API
[ ] Route map visualisation
[ ] Stop markers
[ ] Route shape rendering
[ ] Journey search interface
[ ] RAPTOR routing implementation
[ ] Journey result visualisation
[ ] Free Tram Zone detection
[ ] Dockerised deployment
```

## Why I Built This

MelbourneTransit started as a way for me to learn full-stack development by working with a real transport dataset instead of building another small CRUD application.

The project gives me a practical environment to work with:

- REST API design
- relational and spatial databases
- backend architecture
- data engineering
- React
- mapping
- transport algorithms
- algorithm design and optimisation

As the project grows, I plan to move further into routing algorithms and backend system design while keeping the application usable as a real Melbourne transport tool.

## Data

The project uses public transport GTFS datasets for Victoria.

GTFS data itself is not stored in this repository. Users should obtain the relevant datasets separately and load them locally using the provided data-processing scripts.

## Status

MelbourneTransit is actively under development.

The current focus is building the core route, stop, and map functionality before implementing the journey-planning engine.

## Author

**La Gia Phuc**

Bachelor of Computer Science  
La Trobe University
