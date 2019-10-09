#https://codechalleng.es/bites/145/

from collections import namedtuple
from datetime import date, datetime
import os

import pandas as pd
import urllib

DATA_FILE = "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")

def get_dataframe_from_csv_file(season=1):
    season_script = os.path.join('/tmp', 'seasons_script.csv')
    urllib.request.urlretrieve(DATA_FILE.format(season), season_script)
    with open(season_script) as data_file:
        data = pd.read_csv(data_file)
    return data

def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    data = get_dataframe_from_csv_file()
    data.Date = data.Date.astype('datetime64[ns]')
    data = data.sort_values(by=['Date', 'ID'])
    mask_date_range = ((data['Date'] >= '2015-01-01') & (data['Date'] <= '2015-12-31'))
    data_2015 = data.loc[mask_date_range]

    min_mask = data_2015['Data_Value'].idxmin()
    max_mask = data_2015['Data_Value'].idxmax()

    min_data = data_2015.loc[min_mask]
    max_data = data_2015.loc[max_mask]

    return (STATION(max_data['ID'],
                    date(max_data['Date'].year,
                         max_data['Date'].month,
                         max_data['Date'].day),
                    float(max_data['Data_Value'])/10),
            STATION(min_data['ID'],
            date(min_data['Date'].year,
                 min_data['Date'].month,
                 min_data['Date'].day
            ), float(min_data['Data_Value'])/10))

if __name__ == '__main__':
    print(high_low_record_breakers_for_2015())