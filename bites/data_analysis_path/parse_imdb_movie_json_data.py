import glob
import json
import os
import operator
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movies_list = list()
    for file in files:
        with open(file) as f:
            movies_list.append(json.loads(f.read()))
    return movies_list

def get_single_comedy(movies):
    return[movie['Title'] for movie in movies if 'Comedy' in movie['Genre']][0]
        
def get_movie_most_nominations(movies):
    nominations_count = dict()
    for movie in movies:
        nominations_count[movie['Title']] = sum([int(nom) for nom in movie['Awards'].split() if nom.isdigit()])
    return max(nominations_count.items(), key=operator.itemgetter(1))[0]


def get_movie_longest_runtime(movies):
    runtime_count = dict()
    for movie in movies:
        runtime_count[movie['Title']] = sum([int(runtime) for runtime in movie['Runtime'].split() if runtime.isdigit()])
    return max(runtime_count.items(), key=operator.itemgetter(1))[0]

if __name__ == "__main__":
    movies_list = get_movie_data()
    get_single_comedy(movies_list)
    get_movie_most_nominations(movies_list)
    get_movie_longest_runtime(movies_list)