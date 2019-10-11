#https://codechalleng.es/bites/170/

import pandas as pd
import urllib
import os

DATA = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object


def get_dataframe_from_csv_file():
    mcdo_data_file = os.path.join('/tmp', 'mcdo_data.csv')
    if not os.path.isfile(mcdo_data_file):
        urllib.request.urlretrieve(DATA, mcdo_data_file)
    with open(mcdo_data_file) as data_file:
        data = pd.read_csv(data_file)
        pd.options.mode.chained_assignment = None  # ignore warnings
    return data


df = get_dataframe_from_csv_file()


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    return df.loc[df['Calories'].idxmax()]['Item']


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    df = df.loc[df['Calories'].to_numpy().nonzero()]
    df['Body_Ratio'] = [row['Protein']/row['Calories'] for index, row in df.iterrows()]

    if excl_drinks:
        mask = df['Category'].isin(['Coffee & Tea', 'Beverages'])
        df = df[~mask]

    df = df.sort_values(by=['Body_Ratio'], ascending=False)
    return [row ['Item'] for index, row in df.head().iterrows()]


if __name__ == '__main__':
    print(get_bodybuilder_friendly_foods())
    print(get_bodybuilder_friendly_foods(excl_drinks=True))