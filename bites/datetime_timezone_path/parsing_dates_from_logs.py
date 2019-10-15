# https://codechalleng.es/bites/7/

from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    date = line.split(' ')[1]
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shudowns = [line for line in loglines if SHUTDOWN_EVENT in line]
    date_first = convert_to_datetime(shudowns[0])
    date_last = convert_to_datetime(shudowns[-1])
    return date_last - date_first


if __name__ == "__main__":
    time_between_shutdowns(loglines)