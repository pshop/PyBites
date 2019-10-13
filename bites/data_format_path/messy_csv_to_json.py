# https://codechalleng.es/bites/150/

import json
import csv
from io import StringIO

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


def convert_to_json(members=members):
    members_cleaned = StringIO(members.replace(';', ',').replace('|', ',').strip())
    reader = csv.reader(members_cleaned, delimiter=',')

    keys = list()
    members_list = list()

    for index, row in enumerate(reader):
        if index == 0:
            keys = row
        else:
            members_list.append({key: row for key, row in zip(keys, row)})
    return json.dumps(members_list)


if __name__ == '__main__':
    print(convert_to_json())