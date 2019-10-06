import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    movies_by_director = dict()

    with open(MOVIE_DATA) as file:
        movies_dict = csv.DictReader(file)

        for movie in movies_dict:
            if movie['title_year'] is not '' and\
                int(movie['title_year']) >= MIN_YEAR and\
                movie['movie_title'] is not '' and\
                movie['imdb_score'] is not '':

                movie_infos = Movie(movie['movie_title'].replace(u'\xa0',u''), int(movie['title_year']), float(movie['imdb_score']))
                if movie['director_name'] not in movies_by_director.keys():
                    movies_by_director[movie['director_name']] = list()
                movies_by_director[movie['director_name']].append(movie_infos)
    return movies_by_director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    m = 0
    for movie in movies:
        m += movie.score
    return round(m/len(movies), 1)




def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    average_scores = list()

    for director in directors:
        if len(directors[director]) >= MIN_MOVIES:
            average_scores.append((director, calc_mean_score(directors[director])))
    return sorted(average_scores, key=lambda tup: tup[1], reverse=True)

if __name__ == '__main__':
    directors_list = get_movies_by_director()
    print(get_average_scores(directors_list))