#https://codechalleng.es/bites/130/

from collections import Counter
from pprint import pprint as pp

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    automaker_of_the_year = Counter()
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    for car in data:
        if car['year'] == int(year):
            automaker_of_the_year[car['automaker']] += 1
    return automaker_of_the_year.most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models_automaker_per_year = set()
    for car in data:
        if car['automaker'] == automaker and\
            car['year'] == int(year):
            models_automaker_per_year.add(car['model'])
    return models_automaker_per_year


if __name__ == "__main__":
    print(most_prolific_automaker(2008))
    print(get_models('Mercedes-Benz', 2000))