#https://codechalleng.es/bites/97/

from collections import defaultdict
import os
from urllib.request import urlretrieve
import pprint

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""

    soup = BeautifulSoup(content, 'html.parser')
    table_soup = soup.find_all('table', class_="list-table")

    for row in table_soup[0].find_all('tr')[1:]:

        listed_row = row.get_text().splitlines()

        month = listed_row[2].split('-')[1]
        days_name = listed_row[5].strip()
        holidays[month].append(days_name)
    return holidays


if __name__ == '__main__':
    pprint.pprint(get_us_bank_holidays())