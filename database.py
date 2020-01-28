import psycopg2
from sqlalchemy import create_engine

HOST = '0.0.0.0'
DATABASE = 'sales'
USER = 'pguser'
PORT = '54320'
PASSWORD = '1234'


def connection():
    try:
        connection = psycopg2.connect (
            user= USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            database=DATABASE
        )
        print(connection.get_dsn_parameters(),"\n")
        return connection
    except psycopg2.Error as ex:
        print("[conectando a db connection]: {}".format(ex))


def conn():
    # connection to db
    try:
        connect_string = 'postgres://{user}:{password}@{host}:{port}/{database}'.format(
            user=USER, password=PASSWORD, host=HOST, database=DATABASE, port=PORT)
        sql_engine = create_engine(connect_string, echo=False)
        print(connect_string)
        return sql_engine
    except psycopg2.Error as ex:
        print('[Conn]: ', ex)

#
# def write():
#     try:
#         conn = connection()
#         cur = conn.cursor()
#         cur.execute(queries.INSERT_INTO_MASTER)
#         conn.commit()
#         if cur.rowcount < 0:
#             print('mal')
#         else:
#             print('bien')
#     except Exception as error:
#         print("error: {}".format(error))
