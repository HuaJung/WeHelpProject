import mysql.connector


def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="cannot tell you",
        charset='utf-8',
        database='website'
    )


def data_query_one(sql):
    conn = connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
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


def insert_or_update(sql):
    conn = connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()


