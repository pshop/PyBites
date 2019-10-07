#https://codechalleng.es/bites/90/

import csv
import os
import re
import urllib.request
from collections import Counter, defaultdict
from pprint import pprint as pp


SEASON_URL = 'https://raw.githubusercontent.com/BobAdamsEE/SouthParkData/master/by-season/Season-{}.csv'

def get_season_csv_file(season=1):
    season_script = os.path.join('/tmp', 'seasons.csv')
    urllib.request.urlretrieve(SEASON_URL.format(season), season_script)
    with open(season_script) as sc:
        sc_reader = csv.reader(sc)
        for line in sc_reader:
            yield line

def get_num_words_spoken_by_character_per_episode(content):
    talk_counter = defaultdict(Counter)
    regex = re.compile('[^a-zA-Z ]')
    for line in content:
        if 'Seanson' not in line[0]:
            talk_counter[line[2]][line[1]] += len(line[3].split())
    pp(talk_counter)
            




if __name__ == "__main__":
    season_file = get_season_csv_file(1)
    get_num_words_spoken_by_character_per_episode(season_file)

    