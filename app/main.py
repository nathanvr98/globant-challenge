from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from mangum import Mangum
from app.explore_db import (
    execute_sql_queries,
    hired_employees_by_quarter,
    high_performing_departments,
)
from app.csv_to_db import migrate_table


# Create a FastAPI instance
app = FastAPI()

handler = Mangum(app)


@app.get("/hello")
async def hello():
    return {"message": "Hello, world!"}


@app.get("/setup-db")
async def setup_db():
    sql_files = [
        "create_departments_table",
        "create_jobs_table",
        "create_employees_table",
    ]

    for sql_file in sql_files:
        execute_sql_queries(sql_file)

    return {"message": "Queries executed, tables created"}


@app.post("/upload/{table_name}")
async def upload_data(table_name: str):
    supported_tables = ["departments", "employees", "jobs"]

    if table_name not in supported_tables:
        raise HTTPException(
            status_code=400, detail=f"Table {table_name} not supported."
        )

    try:
        migrate_table(table_name)
        return {"message": f"Data uploaded successfully to table {table_name}."}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error uploading data to table {table_name}: {str(e)}",
        )


@app.get("/employees-by-quarter")
async def get_employees_by_quarter():
    try:
        results = hired_employees_by_quarter()
        return JSONResponse(content=results, status_code=200)
    except Exception as e:
        return JSONResponse(
            {"error": f"Error getting the data: {str(e)}"}, status_code=500
        )


@app.get("/high-performing-departments")
async def get_high_performing_departments():
    try:
        results = high_performing_departments()
        return JSONResponse(content=results, status_code=200)
    except Exception as e:
        return JSONResponse(
            {"error": f"Error getting the data: {str(e)}"}, status_code=500
        )
