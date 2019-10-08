#https://codechalleng.es/bites/48/

import os
import urllib.request

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    with open(LOG) as log:
        l = log.read()
        l = l.splitlines()

    # line : 02-22 23:59 root         DEBUG    - cached, skipping
    day_line = l[0].split(' ')[0] + ' ' # = '02-22 '

    for index, line in enumerate(l):
        if day_line.split(' ')[0] not in line.split(' ')[0]:
                #if day not empty '02-22 ' = 6 chars
                if len(day_line) > 6:
                    print(day_line)
                day_line = l[index].split(' ')[0] + ' '
        if 'sending to slack channel' in line:
            if 'Python' in l[index-1]:
                day_line += PY_BOOK
            else:
                day_line += OTHER_BOOK
    print(day_line)
        

                

if __name__ == "__main__":
    create_chart()