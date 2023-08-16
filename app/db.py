import os
from sqlalchemy import create_engine
import logging

# Read connection configuration from environment variables
conn = {
    "login": os.environ.get("DB_LOGIN"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT", "5432"),
    "schema": os.environ.get("DB_SCHEMA", "globant")
}

# Create database connection
def create_db_connection():
    """
    Create a database connection using the provided configuration.

    Returns:
        sqlalchemy.engine.base.Engine: A database engine object.
    """
    # Build DB URL
    db_url = f"postgresql+psycopg2://{conn['login']}:{conn['password']}@{conn['host']}:{conn['port']}/{conn['schema']}"

    # Connect to the database
    try:
        engine = create_engine(db_url)
        logging.info("Database connection established")
        return engine
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        raise

# Execute SQL queries from a file
def execute_sql_queries(sql_file_name):
    """
    Execute SQL queries from a file.

    Args:
        sql_file_name (str): The name of the SQL file (without extension).
    """
    file_path = os.path.abspath(os.path.join("app", "ddl_scripts", f"{sql_file_name}.sql"))
    with open(file_path, "r") as file:
        query = file.read()
        engine = create_db_connection()
        cursor = engine.connect().cursor()
        cursor.execute(query)
        cursor.close()
        engine.dispose()

