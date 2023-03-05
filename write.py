from util import get_connection
from read import read_table
import pandas as pd
import logging

def insert_data_to_table(connection, cursor, query, data, batch_size=100):
    buffer_data = []
    records_inserted = 0
    for record in data:
        if len(buffer_data) < batch_size:
            buffer_data.append(record)
        else:
            cursor.executemany(query, buffer_data)
            connection.commit()
            records_inserted += len(buffer_data)
            buffer_data = []
    # write any remaining data 
    cursor.executemany(query, buffer_data)
    connection.commit()
    logging.info(f"Number of records inserted into table - {records_inserted + len(buffer_data)}")

def load_table(db_details, column_names, data, table_name, append=True):
    "Helps to read table from the database tables"
    # create connection
    connection = get_connection(db_details["DB_TYPE"], db_details["DB_HOST"], db_details["DB_NAME"], db_details["DB_USER"], db_details["DB_PASS"])
    # create a cursor
    cursor = connection.cursor()
    try:
        if not append:
            cursor.execute(f"TRUNCATE {table_name}")
            connection.commit()
        col_s = ','.join(column_names)
        _s = ','.join(('%s',)*len(column_names))
        query = f"INSERT INTO {table_name} ({col_s}) VALUES ({_s})"
        insert_data_to_table(connection, cursor, query, data)
    except Exception as e:
        logging.error(f"Could not execute the query - {e}")
        data=[],
        cols=[]
    
    connection.close()
    
def test_load_table(db_details_target):
    load_table(db_details_target, ('id', 'name'), [[1, 'test_case']], 'test', False)
    
    # read a table from postgres
    logging.info("Reading test from target")
    cols, data = read_table(db_details_target, "test", 5)
    # print as a DF
    print(pd.DataFrame(data, columns=cols))
    
    