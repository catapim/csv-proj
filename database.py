import psycopg2
from sqlalchemy import create_engine

HOST = 'localhost'
DATABASE = 'sales'
USER = 'admin'
PORT = '3306'
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
    except Exception as error:
        print("[conectando a db connection]: {}".format(error))


def conn():
    # connection to db
    try:
        connect_string = 'postgres://{user}:{password}@{host}/{database}'.format(
            user=USER, password=PASSWORD, host=HOST, database=DATABASE)
        sql_engine = create_engine(connect_string, echo=False)
        print ('[Conn]: success')
        return sql_engine
    except Exception as ex:
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
