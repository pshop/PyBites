# https://codechalleng.es/bites/28/

import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/dates/'
RSS_FEED = 'all.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = '/tmp'


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    if type(date_str) is str:
        date_str = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
    return date_str.replace(tzinfo=None)

# OFFICIAL SOLUTION # NOTCOOL
# def convert_to_datetime(date_str):
#     """Receives a date str and convert it into a datetime object"""
#     date_str = date_str.split('+')[0].strip()
#     # for tz aware wrap dt in pytz.utc.localize (tests support it)
#     return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S')

def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    month_counter = collections.Counter()
    for date in dates:
        date = convert_to_datetime(date)
        month_counter[f"{date.strftime('%Y')}-{date.strftime('%m')}"] += 1
    return month_counter.most_common()[0][0]

# OFFICIAL SOLUTION # NOTCOOL
# def get_month_most_posts(dates):
#     """Receives a list of datetimes and returns the month (format YYYY-MM)
#        that occurs most"""
#     year_months = [f'{d.year}-{str(d.month).zfill(2)}' for d in dates]
#     cnt = collections.Counter(year_months)
#     return cnt.most_common(1)[0][0]

if __name__ == "__main__":
    print(get_month_most_posts(_get_dates()))