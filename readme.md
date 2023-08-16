# Globant API

This is a simple FastAPI API for Globant Data Engineer Challenge. It can be used to create, read, update, and delete departments, jobs, and employees.

## Getting Started

1. Install Docker and Docker Compose.
2. Clone this repository.
3. In the project directory, run `docker-compose up`.
4. The API will be available at http://localhost:9000.

## Endpoints

The following endpoints are available:

- `/hello` - Returns a greeting message.
- `/setup-db` - Creates the database tables.
- `/upload/{table_name}` - Uploads data to the specified table. Supported tables are: departments, employees, and jobs.

## Documentation

The API documentation is available at http://localhost:9000/docs.