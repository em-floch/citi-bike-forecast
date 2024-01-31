import concurrent.futures
import glob
import pandas as pd
import logging
import os
logger = logging.getLogger(__name__)

def standardize_columns(df):
    df.columns = (
        df.columns.str.lower())
    col_to_rename = {'starttime': 'start time', 'stoptime': 'stop time', 'tripduration': 'trip duration', 'bikeid':'bike id', 'usertype': 'user type',
                     'started_at': 'start time', 'ended_at': 'stop time',
                     'start_lat': 'start station latitude', 'start_lng': 'start station longitude',
                     'end_lat': 'end station latitude', 'end_lng': 'end station longitude'}
    df = df.rename(columns=col_to_rename)
    cols = ['_'.join(col.split()) for col in df.columns]
    df.columns = cols
    return df

def groupby_start_time(df):
    df_count = df.groupby(['start_time']).size().reset_index(name='count')
    df_count['start_time'] = pd.to_datetime(df_count['start_time'])
    df_count = df_count.set_index('start_time')
    df_count = df_count.resample('D').sum().fillna(0)
    return df_count


def get_count_per_day(path):
    logger.info(f'Processing {path}')
    df = pd.read_csv(path)
    df = standardize_columns(df)
    df_count = groupby_start_time(df)
    return df_count


def load_data(data_path):
    file_paths = glob.glob(os.path.join(data_path, '*tripdata.csv'))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(get_count_per_day, file_paths)
        concatenated_df = pd.concat(results)
    return concatenated_df


if __name__ == "__main__":
    df = load_data(data_path='../data')
    df.to_csv('../data/citi_bike_data_sample.csv')