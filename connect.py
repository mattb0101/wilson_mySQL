import mysql.connector
from mysql.connector import Error


def connect():
    """ connect to the MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                        user='root',
                                        password='ftK52yA7#010190')
        if conn.is_connected():
            print("Connected to MySQL database")

    except Error as e:
        print(e)
    
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()

