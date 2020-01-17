import pandas as pd 
import csv
from pandas import DataFrame

ORIGINAL_FILE = 'meteorite-landings.csv'
OUTPUT_COLUMNS = 'output.csv'

pd.options.display.max_rows=5

def read_original_csv():
    read_csv = pd.read_csv(ORIGINAL_FILE)
    return read_csv
    # print(read_csv)

def read_filtered_csv():
    read_filter = pd.read_csv(ORIGINAL_FILE, usecols=['name','id','nametype','fall','GeoLocation'])
    return read_filter
    # print(read_filter)

def write_to_csv(read_filter):
    df = DataFrame(read_filter)
    output_file = df.to_csv(OUTPUT_COLUMNS)
    return output_file

def return_dataframe(read_filter):
    df = DataFrame(read_filter)
    return df

def aggregate_csv(data_frame):
    data_frame.groupby('name').aggregate('median').to_csv('new.csv')

def filter_csv(file_to_read):
    df = pd.read_csv(ORIGINAL_FILE, sep=',')
    df.groupby(['id'], as_index=False)
    df_filtered=df.query('id<10')
    df_filtered.to_csv('filtrado.csv',index=False)



read_original_csv()
read_filtered_csv()
write_to_csv(read_filtered_csv())
aggregate_csv(return_dataframe(read_original_csv()))
filter_csv(ORIGINAL_FILE)