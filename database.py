import sql
import pymysql as pymysql
import os
import queries
import mysql.connector as mariadb
from mysql.connector import errorcode


def connection():
    try:
        mariadb_connection = mariadb.connect(
            host='localhost',
            database='sales',
            user='admin',
            password='1234',
        )
        return mariadb_connection
    except Exception as error:
        print("error: {}".format(error))
 


def write():
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute(queries.INSERT_INTO_MASTER)
        conn.commit()
        if cur.rowcount < 0:
            print('mal')
        else:
            print('bien')
    except Exception as error:
        print("error: {}".format(error))
