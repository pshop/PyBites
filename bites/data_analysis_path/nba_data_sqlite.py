from collections import namedtuple, Counter
import csv
from pathlib import Path
import sqlite3

import requests

DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP = Path('/tmp')
DB = TMP / 'nba.db'

Player = namedtuple('Player', ('name year first_year team college active '
                               'games avg_min avg_points'))

conn = sqlite3.connect(str(DB))
cur = conn.cursor()


def import_data():
    with requests.Session() as session:
        content = session.get(DATA_URL).content.decode('utf-8')

    reader = csv.DictReader(content.splitlines(), delimiter=',')

    players = []
    for row in reader:
        players.append(Player(name=row['Player'],
                              year=row['Draft_Yr'],
                              first_year=row['first_year'],
                              team=row['Team'],
                              college=row['College'],
                              active=row['Yrs'],
                              games=row['Games'],
                              avg_min=row['Minutes.per.Game'],
                              avg_points=row['Points.per.Game']))

    cur.execute('''CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)''')
    cur.executemany('INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)', players)
    conn.commit()


if DB.stat().st_size == 0:
    print('loading data')
    import_data()


# you code:

def player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    cur.execute("select name, MAX(CAST(avg_points as decimal )) from players;")
    return cur.fetchone()[0]


def number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    cur.execute("SELECT COUNT(*) FROM players WHERE college = 'Duke University';")
    return cur.fetchone()[0]


def avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    cur.execute("SELECT avg(active) FROM players WHERE college = 'Stanford University';")
    return cur.fetchone()[0]


def year_with_most_drafts():
    """Return the year with the most drafts, in SQL you can use GROUP BY"""
    cur.execute("SELECT year, count(*) FROM players group by year;")
    draft_years = Counter()
    for result in cur.fetchall():
        draft_years[result[0]] += result[1]
    return draft_years.most_common()[0][0]

if __name__ == '__main__':
    year_with_most_drafts()