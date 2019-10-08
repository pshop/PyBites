# https://codechalleng.es/bites/129/

import requests
import json
from collections import defaultdict, Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    value = cap.strip('$')
    if 'M' in value:
        return float(value.strip('M'))
    elif 'B' in value:
        return float(value.strip('B')) * 1000
    else:
        return 0
    

def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    cap_sums = defaultdict()
    return round(
        sum(
            [_cap_str_to_mln_float(line['cap']) for line in data if line['industry'] == industry]
        ),2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    stock_symbol_cap = Counter()
    for line in data:
        stock_symbol_cap[line['symbol']] += _cap_str_to_mln_float(line['cap'])
    return stock_symbol_cap.most_common(1)[0][0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sector_cap = Counter()
    for line in data:
        sector_cap[line['sector']] += _cap_str_to_mln_float(line['cap'])
    max_min_cap = (sector_cap.most_common(1)[0][0], sector_cap.most_common()[-1][0])
    return max_min_cap

if __name__ == "__main__":
        get_sectors_with_max_and_min_stocks()