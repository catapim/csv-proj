import pandas as pd
from pandas import DataFrame
import database
import queries
import sqlalchemy as sql
import numpy as np

ORIGINAL_FILE = 'records.csv'
OUTPUT_FILE = 'output.csv'
FILTERED_FILE = 'filtered.csv'
FILTERED_REGION_COUNTRY = 'filtered_region_country.csv'
AGG_FILE = 'agg.csv'
FILTERED_TO_CSV = 'filteredtocsv.csv'

pd.options.display.max_rows = 10




# connection to maria db
try:
    connect_string = 'mysql+pymysql://admin:1234@localhost/sales'
    sql_engine = sql.create_engine(connect_string, echo=False)

except Exception as error:
    print(error)


# reads and return original csv
def read_original_csv():
    read_csv = pd.read_csv(ORIGINAL_FILE)
    return read_csv


# reads original csv and writes it in maria db
def write_all_data(read_csv):
    try:
        df = pd.DataFrame(read_csv)
        df.columns.values[0] = 'id'
        df['id'] = df.index + 1
        df.to_sql('all_data', con=sql_engine, schema=None, if_exists='replace', index=False)
        sql_engine.execute('''
            SELECT * FROM all_data
        ''').fetchall()
    except Exception as error:
        print('write_all_data error: ', error)


# reads original csv and gets region and country
# it creates a new csv with the previous data
# then a table is created in a database with the data from the csv
def read_write_region_data(read_csv):
    try:
        df = pd.DataFrame(read_csv)
        main_data = pd.read_csv(ORIGINAL_FILE, usecols=['Region', 'Country'])
        df = pd.DataFrame(main_data)
        region_country_data = df.drop_duplicates(keep='last')
        region_country_data = DataFrame(region_country_data, columns=['Region', 'Country']).reset_index()
        region_country_data.columns.values[0] = 'ID'
        region_country_data['ID'] = region_country_data.index + 1
        region_country_data.to_csv(FILTERED_REGION_COUNTRY, sep=',', index=False)
        region_country_data.to_sql('master_country', con=sql_engine, schema=None, if_exists='replace', index=False)
        sql_engine.execute('''
            SELECT * FROM master_country''').fetchall()
    except Exception as error:
        print('error: ', error)


# reads original csv and return only the cols indicated
def read_to_filter(file_to_read):
    try:
        df = pd.read_csv(file_to_read)
        df__ = df.filter(["Country", "Item Type", "Units Sold", "Total Revenue"])
        df__ = df__[(df__['Units Sold'].astype(int) < 5000)]

        df__.to_csv(FILTERED_TO_CSV, index=False)
        print(df__)
        return df__
    except Exception as error:
        print('error: ', error)


def file_to_aggregate(file_to_read):
    try:
        df = pd.read_csv(FILTERED_TO_CSV)
        df = df.agg({'Units Sold': ['min', 'max'],
                      "Total Revenue" : ['min', 'max']})
        df.to_csv('test.csv')
        print(df)

    except Exception as ex:
        print('[file to aggregate] Exception: ', ex)


# read filtered data and write it in new csvbkn
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


database.write()
read_original_csv()
# write_all_data(read_original_csv())
# read_write_region_data(read_original_csv())
read_to_filter(ORIGINAL_FILE)
file_to_aggregate(FILTERED_TO_CSV)
# write_to_csv(read_to_filter(read_original_csv()))
# aggregate_csv(return_dataframe(read_original_csv()))
# filter_csv(ORIGINAL_FILE)
# set_master_data(read_original_csv()) '
print('done')
