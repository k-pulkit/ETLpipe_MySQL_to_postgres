import logging
import pandas as pd
from config import DB_DETAILS
import mysql.connector as mysql
from mysql.connector import errorcode as mysql_errors
import psycopg2 as postgres
from psycopg2 import errorcodes as postgres_errors

def get_tables():
    "Loads the list of tables to load to target"
    tables = pd.read_csv('./tablelist.txt', sep=':').query('to_be_loaded=="yes"')
    return tables

def get_db_details(env):
    "Returns the connection info for the database connections"
    return DB_DETAILS.get(env, None)

def get_mysql_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    except mysql.Error as error:
        if error.errno == mysql_errors.ER_ACCESS_DENIED_ERROR:
            logging.error("Error establishing the connection to mysql. Reason invalid credentials")
        else:
            logging.error(f"Unable to connect - {error}")
    return connection

def get_postgres_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = postgres.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
    except postgres.OperationalError as error:
        if error.errno == postgres_errors.INVALID_PASSWORD or error.errno == postgres_errors.INVALID_AUTHORIZATION_SPECIFICATION:
            logging.error("Error establishing the connection to postgres. Reason invalid credentials")
        else:
            logging.error(f"Unable to connect - {error}")
    return connection

def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection=None
    if db_type == "mysql":
        return get_mysql_connection(db_host, db_name, db_user, db_pass)
    elif db_type == "postgres":
        return get_postgres_connection(db_host, db_name, db_user, db_pass)
    else:
        raise KeyError("db_type should be from mysql, postgres")



