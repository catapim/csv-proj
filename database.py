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
        print("[conectando a db connection] exception:  {}".format(ex))
