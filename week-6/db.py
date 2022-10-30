import mysql.connector
from mysql.connector import errorcode


def connection():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="cannot tell you",
            charset='utf-8',
            database='website',
            raise_on_warnings=True
        )
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)


def data_query_one(sql, condition):
    conn = connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, condition)
        return cursor.fetchone()
    finally:
        conn.close()


def data_query_all(sql):
    conn = connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()


def insert_or_update(sql, condition):
    conn = connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, condition)
        conn.commit()
    finally:
        conn.close()


