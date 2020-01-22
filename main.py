import pandas as pd
from pandas import DataFrame
import database
import queries
import sqlalchemy as sql


ORIGINAL_FILE = 'records.csv'
OUTPUT_COLUMNS = 'output.csv'

pd.options.display.max_rows = 200
# conn = database.connection()

try:
    connect_string = 'mysql+pymysql://admin:1234@localhost/sales'
    sql_engine = sql.create_engine(connect_string, echo=False)

except Exception as error:
    print(error)


# lee el original
def read_original_csv():
    read_csv = pd.read_csv(ORIGINAL_FILE)
    return read_csv


def set_master_data(read_csv):
    df = pd.DataFrame(read_csv)
    main_data = pd.read_csv(ORIGINAL_FILE, usecols=['Region', 'Country'])
    df = pd.DataFrame(main_data)
    filtered_main_data = df.drop_duplicates(keep='last')
    filtered = DataFrame(filtered_main_data, columns=['Region', 'Country'])
    # filtered_main_data.to_csv('filteredmaster.csv', sep=',', index=False)
    try:
        filtered_main_data.to_sql('master_country', con=sql_engine, schema=None, if_exists='replace', index=False)
        sql_engine.execute('''
            SELECT * FROM master_country''').fetchall()
    except Exception as error:
        print('error: ', error)


def read_to_filter():
    read_filter = pd.read_csv(ORIGINAL_FILE, usecols=['Region', 'Item Type', 'Order Priority', 'Ship Date', 'Unit Cost', 'Total Revenue'])
    return read_filter


def write_to_csv(read_filter):
    df = DataFrame(read_filter)
    output_file = df.to_csv(OUTPUT_COLUMNS, sep=',', index=False)
    return output_file


def return_dataframe(read_filter):
    df = DataFrame(read_filter)
    return df


def filter_csv(file_to_read):
    df = pd.read_csv(ORIGINAL_FILE, sep=',')
    df.filter(items=None, like='Order Priority', regex=None, axis=None)
    df.groupby(['id'], as_index=False)
    df_filtered = df.query('id<10')
    df_filtered.to_csv('filtrado.csv', index=False)


# def aggregate_csv(data_frame):
#     data_frame.groupby('name').agg(axis=0, 'mean').to_csv('new.csv')
#


database.write()
# read_original_csv()
# read_to_filter()
# write_to_csv(read_to_filter())
# # aggregate_csv(return_dataframe(read_original_csv()))
# # filter_csv(ORIGINAL_FILE)
set_master_data(read_original_csv())