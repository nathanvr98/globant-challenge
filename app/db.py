import os
import logging
import psycopg2
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)

load_dotenv()

# Read connection configuration from environment variables
conn = {
    "login": os.environ.get("DB_LOGIN", "postgres"),
    "password": os.environ.get("DB_PASSWORD", "postgres"),
    "host": os.environ.get("DB_HOST", "db"),
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
