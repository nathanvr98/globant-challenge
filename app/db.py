import os
from sqlalchemy import create_engine
import logging
import psycopg2
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)

load_dotenv()

# Read connection configuration from environment variables
conn = {
    "login": os.environ.get("DB_LOGIN"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT", "5432"),
    "schema": os.environ.get("DB_SCHEMA", "globant")
}

def create_db_connection():
    """
    Create a database connection using the provided configuration.

    Returns:
        psycopg2.extensions.connection: A database connection object.
    """
    # Read connection configuration from environment variables

    # Build DB URL
    db_url = f"dbname='{conn['schema']}' user='{conn['login']}' password='{conn['password']}' host='{conn['host']}' port='{conn['port']}'"

    # Connect to the database
    try:
        connection = psycopg2.connect(db_url)
        logging.info("Database connection established")
        return connection
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

