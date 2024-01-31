# Scarpe data from https://s3.amazonaws.com/tripdata/201509-citibike-tripdata.csv.zip

import os
import glob
import zipfile
import urllib.request
from urllib.error import HTTPError
from tqdm import tqdm


def download_data_one_month(year, month, output_path):
    month = str(month).zfill(2)
    if year < 2017:
        url = f'https://s3.amazonaws.com/tripdata/{year}{month}-citibike-tripdata.zip'
        file_name = f'{year}{month}-citibike-tripdata.zip'
    else:
        url = f'https://s3.amazonaws.com/tripdata/{year}{month}-citibike-tripdata.csv.zip'
        file_name = f'{year}{month}-citibike-tripdata.csv.zip'

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file = os.path.join(output_path, file_name)
    try:
        urllib.request.urlretrieve(url, output_file)
    except HTTPError as e:
        print(f'Failed to download file for {year}-{month}, {e}')
    else:
        with zipfile.ZipFile(output_file, 'r') as zip_ref:
            zip_ref.extractall(output_path)
        os.remove(output_file)
    print(f'Downloaded file for {year}-{month}')

def download_all_data(output_path, start_year, end_year):
    for year in tqdm(range(start_year, end_year+1), desc='Year'):
        for month in range(1, 13):
            download_data_one_month(year, month, output_path)


if __name__ == "__main__":
    download_all_data(output_path='../data', start_year=2021, end_year=2023)