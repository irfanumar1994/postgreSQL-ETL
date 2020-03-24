import psycopg2
from Create_Table_queries import create_table_queries, drop_table_queries


def create_database():
    '''Creates and connects to youtube  database. Returns cursor and connection to DB'''
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 user=postgres password=12345678")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create youtube database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS youtubedb")
    cur.execute("CREATE DATABASE Youtubedb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to youtubedb database
    conn = psycopg2.connect("host=127.0.0.1 dbname=youtubedb user=postgres password=12345678")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    '''Drops all tables created on the database'''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''Created tables defined on the Create_Table_queries script'''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ Function to drop and re create youtube database and all related tables.
        Usage: python Create_Table_queries.py
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()
    
main()
