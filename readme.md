# Globant API

This is a simple FastAPI API for Globant Data Engineer Challenge. It can be used to create, read, update, and delete departments, jobs, and employees.

## Getting Started

1. Install Docker and Docker Compose.
2. Clone this repository.
3. In the project directory, run `docker-compose up`.
4. The API will be available at http://localhost:9000.
5. The Postgres will be available at http://localhost:5432.


#  Section 1: API

In the context of a DB migration with 3 different tables (departments, jobs, employees) , create
a local REST API that must:

1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one request

The following endpoints are available:

- `/hello` - Returns a greeting message.
- `/setup-db` - Creates the database tables employees, jobs and departments using the queries inside ddl_scripts.


# Section 2: SQL

You need to explore the data that was inserted in the previous section. The stakeholders ask
for some specific metrics they need. You should create an end-point for each requirement.

The following endpoints are available:

- `/employees-by-quarter` - Number of employees hired for each job and department in 2021 divided by quarter. The
table must be ordered alphabetically by department and job.
- `/high-performing-departments` - List of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments, ordered
by the number of employees hired (descending).

# Code quality
- For ensuring code quality the app uses flake8, black and mypy.
- Run ./code-format.sh in order to run the quality checks.
## Documentation

The API documentation is available at http://localhost:9000/docs.