import pandas as pd
from pandas import DataFrame
import sql_statements as sql
import database as db

# import databasep as db

ORIGINAL_FILE = 'records2.csv'
OUTPUT_FILE = 'output.csv'
FILTERED_FILE = 'filtered.csv'
FILTERED_REGION_COUNTRY = 'filtered_region_country.csv'
AGG_FILE = 'agg.csv'
FILTERED_TO_CSV = 'filteredtocsv.csv'
AGGREGATED_FILE = 'aggregated.csv'

pd.options.display.max_rows = 10


db_conn = db.conn()


# reads original csv and writes it in maria db
def write_all_data(read_csv):
    try:
        df = pd.read_csv(read_csv)
        df.columns.values[0] = 'id'
        df['id'] = df.index + 1
        df.to_sql('all_data', con=db_conn, schema=None, if_exists='replace', index=False)
        db_conn.execute('''
            SELECT * FROM all_data
        ''').fetchall()
        print('[Write all data] ok')
    except Exception as error:
        print('[Write_all_data] error: ', error)

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


def write_all_data_copy():
    try:
        conn = db_conn
        cur = conn.cursor()
        cur.execute(sql.TEST_COPY)
        conn.commit()
        if cur.rowcount < 0:
            print('mal')
        else:
            print('bien')
    except Exception as ex:
        print('[write all data copy] exception', ex)

# reads original csv and gets region and country
# it creates a new csv with the previous data
# then a table is created in a database with the data from the csv
def read_write_region_data(read_csv):
    try:
        df = pd.read_csv(ORIGINAL_FILE, usecols=['Region', 'Country'])
        region_country_data = df.drop_duplicates(keep='last')
        region_country_data = DataFrame(region_country_data, columns=['Region', 'Country']).reset_index()
        region_country_data.columns.values[0] = 'ID'
        region_country_data['ID'] = region_country_data.index + 1
        region_country_data.to_csv(FILTERED_REGION_COUNTRY, sep=',', index=False)
        region_country_data.to_sql('master_country', con=db_conn, schema=None, if_exists='replace', index=False)
        db_conn.execute('''
            SELECT * FROM master_country''').fetchall()
        print('[Read write region data] ok')
    except Exception as ex:
        print('[read_write_region_data]: ', ex)


# reads original csv and return only the cols indicated
def read_to_filter(file_to_read):
    try:
        df = pd.read_csv(file_to_read)
        df = df.filter(["Country", "Item Type", "Units Sold", "Total Revenue"])
        df = df[(df['Units Sold'].astype(int) < 5000)]
        df.to_csv(FILTERED_TO_CSV, index=False)
        print('[Read to filter] Ok')
        return df
    except Exception as ex:
        print('[Read to filter]: Exception ', ex)


def file_to_aggregate(file_to_read):
    try:
        df = pd.read_csv(FILTERED_TO_CSV)
        df = df.agg({'Units Sold': ['min', 'max', 'mean'],
                      "Total Revenue" : ['min', 'max', 'mean']})
        df.to_csv(AGGREGATED_FILE)
        print(df)
    except Exception as ex:
        print('[File to aggregate] Exception: ', ex)


# read filtered data and write it in new csv
# def write_to_csv(read_filter):
#     df = DataFrame(read_filter)
#     output_file = df.to_csv(OUTPUT_FILE, sep=',', index=False)
#     return output_file


# filter original csv
# def filter_csv(file_to_read):
#     df = file_to_read
#     df.filter(items=None, like='Order Priority', regex=None, axis=None)
#     df.groupby(['id'], as_index=False)
#     df_filtered = df.query('id<10')
#     df_filtered.to_csv('filtrado.csv', index=False)


# def aggregate_csv(data_frame):
#     data_frame.groupby('name').agg(axis=0, 'mean').to_csv('new.csv')
#


# database.write()
# read_original_csv()
write_all_data_copy()
# write_all_data(ORIGINAL_FILE)
# read_write_region_data(ORIGINAL_FILE)
# read_to_filter(ORIGINAL_FILE)
# file_to_aggregate(FILTERED_TO_CSV)
# write_to_csv(read_to_filter(read_original_csv()))
# aggregate_csv(return_dataframe(read_original_csv()))
# filter_csv(ORIGINAL_FILE)
# set_master_data(read_original_csv()) '
print('Done')
