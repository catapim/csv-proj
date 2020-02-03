import psycopg2

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
        # print(connection.get_dsn_parameters(),"\n")
        return connection
    except psycopg2.Error as ex:
        print("[conectando a db connection]: {}".format(ex))


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
