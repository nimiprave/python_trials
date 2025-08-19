# Python Database Connection Programs

This repository demonstrates how to connect to different database management systems (DBMS) using Python SQL libraries. You can interact with SQLite, MySQL, and PostgreSQL databases, perform common queries, and develop cross-database applications using Python scripts.

---

## Features

- Connect to SQLite, MySQL, and PostgreSQL databases
- Perform common database queries from Python
- Example scripts for each DBMS
- Environment variable configuration for credentials and paths

---

## PostgreSQL with Docker

### 1. Create a Docker Volume

Create a Docker volume for persistent PostgreSQL data:

```sh
docker volume create postgres_data
```

---

### 2. Run PostgreSQL Container with Volume

Mount the volume to the container's data directory:

```sh
docker run --name postgres_container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=welcome1! \
  -e POSTGRES_DB=postgres \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  -d postgres
```

---

### 3. Verify the Volume

Inspect the container to confirm the volume is mounted:

```sh
docker inspect postgres_container
```

Look for the `"Mounts"` section in the output. It should show:

```json
"Mounts": [
  {
    "Type": "volume",
    "Source": "/var/lib/docker/volumes/postgres_data/_data",
    "Destination": "/var/lib/postgresql/data",
    "Driver": "local",
    "Mode": "rw",
    "RW": true,
    "Propagation": ""
  }
]
```

---

## Environment Parameters

Set these in your `.env` file for local development:

```env
# SQLite
SQLITEPATH=C:\Users\I820262\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db

# SAP HANA
HANA_HOST=lddbede.devsys.net.sap
HANA_PORT=30215
HANA_USER=GAUTHIERA
HANA_PASSWORD=Welcome1!

# PostgreSQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=postgres
POSTGRES_USER=postgres
POSTGRES_PWD=welcome1!
```

---

## Notes

- Replace credentials and paths with your own as needed.
- For other DBMS (MySQL, SAP HANA), see respective Python scripts in this repository.
- Use Docker volumes for persistent data storage.
