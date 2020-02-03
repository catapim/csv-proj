import errno
import os
import pandas as pd
from pandas import DataFrame
import sql_statements as sql
import database as db

# import databasep as db


ORIGINAL_FILE = 'records.csv'
OUTPUT_FILE = 'output.csv'
FILTERED_FILE = 'filtered.csv'
FILTERED_REGION_COUNTRY = 'filtered_region_country.csv'
AGG_FILE = 'agg.csv'
FILTERED_TO_CSV = 'filteredtocsv.csv'
AGGREGATED_FILE = 'aggregated.csv'
CSV_FOLDER = 'csv/'

pd.options.display.max_rows = 10
db_conn = db.connection()


# reads original csv and writes it in maria db
def write_all_data(read_csv):
    try:
        df = pd.read_csv(read_csv)
        # df.columns.values[0] = 'id'
        # df['id'] = df.index + 1
        # df.to_sql('all_data', con=db_conn, schema=None, if_exists='replace', index=False)
        conn = db_conn
        cur = conn.cursor()
        cur.execute(sql.WRITE_ALL_CSV_TO_DB)
        conn.commit()
        # if cur.rowcount <= 0:
        #     print('[write all data] rows smaller or equal to 0')
        # # else:
        # #     print('[write all data] rows added bigger 0')
    except Exception as ex:
        print('[write all data] exception: ', ex)



def write_filtered_data():
    try:
        conn = db_conn
        cur = conn.cursor()
        cur.execute(sql.TEST_COPY)
        conn.commit()
        if cur.rowcount <= 0:
            print('[write all data copy] rows smaller or equal to 0')
        else:
            print('[write all data copy] rows added bigger 0')
    except Exception as ex:
        print('[write all data copy] exception: ', ex)

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
        filename = CSV_FOLDER + '{}'.format(FILTERED_REGION_COUNTRY)
        print(filename)
        create_dir(filename)
        region_country_data.to_csv(filename, sep=',', index=False)
    except Exception as ex:
        print('[read_write_region_data]: ', ex)


# reads original csv and return only the cols indicated
def read_to_filter(file_to_read):
    try:
        df = pd.read_csv(file_to_read)
        df = df.filter(["Country", "Item Type", "Units Sold", "Total Revenue"])
        df = df[(df['Units Sold'].astype(int) < 5000)]
        filename = CSV_FOLDER + '{}'.format(FILTERED_TO_CSV)
        create_dir(filename)
        df.to_csv(filename, index=False)
        print('[Read to filter] Ok')
        return df
    except Exception as ex:
        print('[Read to filter]: Exception ', ex)


def file_to_aggregate(file_to_read):
    try:
        df = pd.read_csv(FILTERED_TO_CSV)
        df = df.agg({'Units Sold': ['min', 'max', 'mean'],
                      "Total Revenue" : ['min', 'max', 'mean']})
        filename = CSV_FOLDER + '{}'.format(AGGREGATED_FILE)
        create_dir(filename)
        df.to_csv(filename)
        print(df)
    except Exception as ex:
        print('[File to aggregate] Exception: ', ex)


def create_dir(dir_name):
    if not os.path.exists(os.path.dirname(dir_name)):
        try:
            os.makedirs(os.path.dirname(dir_name))
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise

# read filtered data and write it in new csv
def write_to_csv(read_filter):
    df = DataFrame(read_filter)
    output_file = df.to_csv(OUTPUT_FILE, sep=',', index=False)
    return output_file


# filter original csv
def filter_csv(file_to_read):
    df = file_to_read
    df.filter(items=None, like='Order Priority', regex=None, axis=None)
    df.groupby(['id'], as_index=False)
    df_filtered = df.query('id<10')
    df_filtered.to_csv('filtrado.csv', index=False)


# def aggregate_csv(data_frame):
#     data_frame.groupby('name').agg(axis=0, 'mean').to_csv('new.csv')
#


write_all_data(ORIGINAL_FILE)
# read_write_region_data(ORIGINAL_FILE)
# read_to_filter(ORIGINAL_FILE)
# file_to_aggregate(FILTERED_TO_CSV)
# write_filtered_data()
print('Done')
