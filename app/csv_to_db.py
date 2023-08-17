import os
import csv
import json
import pandas as pd
import logging
from db import create_db_connection
from dotenv import load_dotenv


load_dotenv()

def get_local_files():
    """
    Get a dictionary of local file paths for each table.

    Returns:
        dict: A dictionary where keys are table names and values are local file paths.
    """
    data_folder = os.path.join(os.path.dirname(__file__), "data")
    return {
        "departments": os.path.join(data_folder, "departments.csv"),
        "jobs": os.path.join(data_folder, "jobs.csv"),
        "employees": os.path.join(data_folder, "employees.csv")
    }

def get_s3_files():
    """
    Get a dictionary of S3 file paths for each table.

    Returns:
        dict: A dictionary where keys are table names and values are S3 file paths.
    """
    bucket_name = "globant-bucket"
    return {
        "departments": f"s3://{bucket_name}/departments.csv",
        "jobs": f"s3://{bucket_name}/jobs.csv",
        "employees": f"s3://{bucket_name}/employees.csv"
    }

def get_column_info_from_json(table_name: str, json_path: str):
    """
    Get column information for a specific table from a JSON file.

    Args:
        table_name (str): The name of the table.
        json_path (str): The path to the JSON file containing column information.

    Returns:
        dict: A dictionary containing column information for the specified table.
    """
    with open(json_path, "r") as json_file:
        data = json.load(json_file)
        table_info = data.get(table_name, None)
    return table_info

def migrate_table_data(cur, table_name: str, column_info: dict, file_path: str):
    """
    Migrate data from a CSV file to a database table.

    Args:
        cur: The database cursor.
        table_name (str): The name of the table.
        column_info (dict): Column information for the table.
        file_path (str): The path to the CSV file.

    """
    print(cur)
    print(table_name)
    try:
        df = pd.read_csv(file_path, delimiter=",", names=column_info["columns"].keys())
        print(df.head())

        if column_info["mode"] == "truncate":
            cur.execute("TRUNCATE TABLE {}".format(table_name))

        batch_size = 1000
        total_rows = df.shape[0]
        for i in range(0, total_rows, batch_size):
            batch = df.iloc[i:i+batch_size]
            placeholders = ", ".join(["%s"] * len(column_info["columns"]))
            insert_query = f"INSERT INTO {table_name} ({', '.join(column_info['columns'])}) VALUES ({placeholders});"
            cur.executemany(insert_query, batch.to_numpy())

    except Exception as e:
        logging.error(e)
        raise e

def migrate_table(table_name: str):
    """
    Migrate data from a CSV file to a database table.

    Args:
        table_name (str): The name of the table.
    """
    conn = create_db_connection()
    print(conn)
    json_path = os.path.join(os.path.dirname(__file__), "columns.json")
    column_info = get_column_info_from_json(table_name, json_path)
    if not column_info:
        raise ValueError(f"Column info for {table_name} not found in JSON.")

    file_path = get_file_path(table_name)
    print(file_path)

    try:
        with conn, conn.cursor() as cur:
            migrate_table_data(cur, table_name, column_info, file_path)
    except Exception as e:
        print("Error during database operation:", e)

def get_file_path(table_name: str):
    """
    Get the file path for a specific table.

    Args:
        table_name (str): The name of the table.

    Returns:
        str: The file path.
    """
    if os.getenv("ENV") == 'LOCAL':
        return get_local_files().get(table_name, None)
    else:
        return get_s3_files().get(table_name, None)

#Code for debug (ignore)    
def main():
    table_name = 'jobs'
    
    try:
        migrate_table(table_name)
        print(f"Datos de la tabla {table_name} migrados exitosamente.")
    except Exception as e:
        print(f"Error al migrar datos de la tabla {table_name}: {e}")

if __name__ == "__main__":
    main()