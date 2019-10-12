#https://codechalleng.es/bites/79/

import csv
import os
import requests
from collections import Counter

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    csv_file = os.path.join('/tmp', 'community.csv')

    if not os.path.isfile(csv_file):
        r = requests.get(CSV_URL)
        with open(csv_file, 'wb') as file:
            csv_file = file.write(r.content)
            for row in csv.reader(file, delimiter=','):
                yield row
    with open(csv_file) as f:
        for row in csv.reader(f, delimiter=','):
            yield row



def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    regions = Counter()
    regions_list = list()
    for user in content:
        regions[user[2]] += 1
        regions_list.append(user[2])

    for region in sorted(set(regions_list)):
        if region != 'tz':
            print(region + (' '*(21-len(region))) + '|' + ('+'*(regions[region])))



if __name__ == '__main__':
    create_user_bar_chart(get_csv())