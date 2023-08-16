from fastapi import FastAPI, HTTPException
import os
import logging
from db import execute_sql_queries
from csv_to_db import migrate_table


# Create a FastAPI instance
app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello, world!"}


@app.get("/setup-db")
async def setup_db():
    sql_files = [
        "create_departments_table",
        "create_jobs_table",
        "create_hired_employees_table",
    ]
    
    for sql_file in sql_files:
        execute_sql_queries(sql_file)
    
    return {"message": "Queries executed, tables created"}

@app.post("/upload/{table_name}")
async def upload_data(table_name: str):
    supported_tables = ["departments", "employees", "jobs"]

    if table_name not in supported_tables:
        raise HTTPException(status_code=400, detail=f"Table {table_name} not supported.")
    
    try:
        migrate_table(table_name)
        return {"message": f"Data uploaded successfully to table {table_name}."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading data to table {table_name}: {str(e)}")

# Evento shutdown para cerrar la conexión a la base de datos al finalizar la API
##@app.on_event("shutdown")
##async def shutdown_db():
##    close_db()
