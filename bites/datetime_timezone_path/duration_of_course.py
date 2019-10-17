from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    times_list = list()
    with open(COURSE_TIMES, 'r') as times:
        for line in times.readlines():
            timestamp = re.findall(r"[0-9]{1,2}:[0-9]{1,2}", line)
            if timestamp != []:
                times_list.append(timestamp[0])
        return times_list
    


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total = timedelta(minutes=0, seconds=0)
    for t in timestamps:
        total += timedelta(minutes=(int(t.split(':')[0])), seconds=(int(t.split(':')[1])))
       
    return total.__str__()


if __name__ == "__main__":
    print(calc_total_course_duration(get_all_timestamps()))