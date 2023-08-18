import os
import logging
from dotenv import load_dotenv
from app.db import create_db_connection

logging.basicConfig(level=logging.INFO)

load_dotenv()


# Execute SQL queries from a file
def execute_sql_queries(sql_file_name):
    """
    Execute SQL queries from a file.

    Args:
        sql_file_name (str): The name of the SQL file (without extension).
    """
    file_path = os.path.abspath(
        os.path.join("app", "ddl_scripts", f"{sql_file_name}.sql")
    )
    with open(file_path, "r") as file:
        query = file.read()
        connection = create_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
            connection.commit()
            logging.info("SQL queries executed successfully")
        except Exception as e:
            logging.error(f"Error executing SQL queries: {e}")
            raise
        finally:
            connection.close()


def hired_employees_by_quarter():
    """
    Execute and SQL query and parse it in a json format.
    """
    file_path = os.path.abspath(os.path.join("app", "sql", "challenge2-1.sql"))
    try:
        with open(file_path, "r") as file:
            query = file.read()
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            connection.commit()
            logging.info("SQL queries executed successfully")
    except Exception as e:
        logging.error(f"Error executing SQL queries: {e}")
        raise
    finally:
        connection.close()

        data = []
        for row in result:
            department_name, job_title, q1, q2, q3, q4 = row
            data.append(
                {
                    "department_name": department_name,
                    "job_title": job_title,
                    "Q1": int(q1),
                    "Q2": int(q2),
                    "Q3": int(q3),
                    "Q4": int(q4),
                }
            )

        return data


def high_performing_departments():
    """
    Execute and SQL query and parse it in a json format.
    """
    file_path = os.path.abspath(os.path.join("app", "sql", "challenge2-2.sql"))
    try:
        with open(file_path, "r") as file:
            query = file.read()
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            connection.commit()
            logging.info("SQL queries executed successfully")
    except Exception as e:
        logging.error(f"Error executing SQL queries: {e}")
        raise
    finally:
        connection.close()

        data = []
        for row in result:
            department_id, department_name, hired = row
            data.append(
                {
                    "department_id": int(department_id),
                    "department_name": department_name,
                    "hired": int(hired),
                }
            )

        return data
