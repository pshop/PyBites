# https://codechalleng.es/bites/160/

import csv
import os
from urllib.request import urlretrieve

BATTLE_DATA = os.path.join('/tmp', 'battle-table.csv')
if not os.path.isfile(BATTLE_DATA):
    urlretrieve('https://bit.ly/2U3oHft', BATTLE_DATA)


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    battle_table_dict = dict()
    with open(BATTLE_DATA) as f:
        battle_table = csv.reader(f)
        for index, row in enumerate(battle_table):
            if index == 0:
                ref = row
            else:
                battle_table_dict[row[0]] = [ref[i] for i, result in enumerate(row) if result == 'win']
    return battle_table_dict

def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()

    if player1 not in defeat_mapping.keys() or \
        player2 not in defeat_mapping.keys():
        raise ValueError

    if player1 == player2:
        return 'Tie'
    if player2 in defeat_mapping[player1]:
        return player1
    else:
        return player2


if __name__ == "__main__":
    print(get_winner('Rock', 'Rock'))