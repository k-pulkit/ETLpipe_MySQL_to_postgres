from util import get_connection
import pandas as pd
import logging

def read_table(db_details, table_name, limit=0):
    "Helps to read table from the database tables"
    # create connection
    connection = get_connection(db_details["DB_TYPE"], db_details["DB_HOST"], db_details["DB_NAME"], db_details["DB_USER"], db_details["DB_PASS"])
    # create a cursor
    cursor = connection.cursor()
    try:
        if limit > 0:
            cursor.execute(f"select * from {table_name} limit {limit}")
        else:
            cursor.execute(f"select * from {table_name}")
        data = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
    except Exception as e:
        logging.error(f"Could not execute the query - {e}")
        data=[],
        cols=[]
    
    connection.close()
    
    return (cols, data)

def def_test_read_table(db_details_source):
    # read a table from mysql
    logging.info("Reading order from source")
    cols, data = read_table(db_details_source, "orders", 5)
    # print as a DF
    print(pd.DataFrame(data, columns=cols))
    
    # write some data to the test table
    