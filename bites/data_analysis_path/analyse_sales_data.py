from os import path
from urllib.request import urlretrieve

import pandas as pd

EXCEL = path.join('/tmp', 'order_data.xlsx')
if not path.isfile(EXCEL):
    urlretrieve('https://bit.ly/2JpniQ2', EXCEL)


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    xls = pd.ExcelFile(excel)
    df = pd.read_excel(xls, 'SalesOrders')
    return df


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df = df.rename(columns={'OrderDate': 'Year'})
    df_total = df.groupby([df['Year'].dt.year, "Region"])['Total'].sum()
    return df_total



def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    df_sales = df.groupby('Rep').sum()
    id_max = df_sales['Total'].idxmax()
    return (id_max, df_sales.loc[id_max]['Total'])

def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    df_item =df.groupby('Item').sum()
    id_max = df_item['Units'].idxmax()
    return (id_max, df_item.loc[id_max]['Units'])

if __name__ == '__main__':
    df = load_excel_into_dataframe()

    print(get_best_sales_rep(df))