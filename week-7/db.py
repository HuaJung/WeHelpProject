import mysql.connector
from mysql.connector import pooling, errorcode


def db_connection():
    db_config = {
        'user': 'root',
        'password': 'cannot tell you',
        'host': 'localhost',
        'database': 'website'
    }
    cnxpool = pooling.MySQLConnectionPool(
        pool_name='week6_pool',
        pool_size=5,
        pool_reset_session=True,
        **db_config
    )
    try:
        cnx = cnxpool.get_connection()
        return cnx
    except mysql.connector.PoolError as err:
        print("Error: {}".format(err))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def data_query_one(sql, condition):
    cnx = db_connection()
    cursor = cnx.cursor()
    try:
        cursor.execute(sql, condition)
        return cursor.fetchone()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        cursor.close()
        cnx.close()


def data_query_all(sql):
    cnx = db_connection()
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        cursor.close()
        cnx.close()


def insert_or_update(sql, condition):
    cnx = db_connection()
    cursor = cnx.cursor()
    try:
        cursor.execute(sql, condition)
        cnx.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        cursor.close()
        cnx.close()

