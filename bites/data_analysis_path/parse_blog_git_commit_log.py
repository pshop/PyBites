from collections import Counter
import os
import re
from urllib.request import urlretrieve
from collections import Counter, defaultdict
from pprint import pprint as pp

from dateutil.parser import parse

commits = os.path.join('/tmp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    change_cnt = Counter()
    with open(commit_log) as logs_file:
        logs = logs_file.read()

        for log in logs.splitlines():
            date = parse(
                re.search(
                    r"(?<=Date:)(.*)(?=\|)", log
                )[0].strip())

            splitted_log = log.split()
            modifs = int(splitted_log[11])
            if len(splitted_log) > 13:
                modifs += int(splitted_log[13])

            if year and date.year == year:
                change_cnt[YEAR_MONTH.format(y=date.year, m=date.month)] += modifs
            elif not year:
                change_cnt[YEAR_MONTH.format(y=date.year, m=date.month)] += modifs

    return (change_cnt.most_common()[-1][0],change_cnt.most_common()[0][0])










if __name__ == '__main__':
    pp(get_min_max_amount_of_commits(year = 2018))