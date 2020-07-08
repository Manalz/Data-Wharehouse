import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

"""
Load staging tables from S3 files using the queries in `copy_table_queries` list.

Parameters: 
arg1 (cur): the curser that is needed to execute the imported required queries (copy_table_queries) 
arg2 (conn): used to commit the copy_table_queries transaction
    
"""
def load_staging_tables(cur, conn):

    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

        
        
"""
Insert tables from S3 staging tables using the queries in `insert_table_queries` list.

Parameters: 
arg1 (cur): the curser that is needed to execute the imported required queries (insert_table_queries) 
arg2 (conn): used to commit the insert_table_queries transaction

"""
def insert_tables(cur, conn):

    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """    
    - Establishes connection with the sparkify database in the redshift cluster and gets
    cursor to it.  
    
    - Load the staging tables by copying them from S3 files.  
    
    - Insert all tables needed. 
    
    - Finally, closes the connection. 
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()