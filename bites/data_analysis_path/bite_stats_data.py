import csv
from os import path
from urllib.request import urlretrieve
from collections import Counter

DATA = path.join('/tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        with open(data) as f:
            rows = csv.DictReader(f)
            return list(rows)

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        accessed = set()
        for row in self.rows:
            accessed.add(row['bite'])
        return len(accessed)

    @property
    def number_bites_resolved(self) -> int:
        resolved = set()
        [resolved.add(row['bite']) for row in self.rows if row['completed'] == 'True']
        return len(resolved)

    @property
    def number_users_active(self) -> int:
        users = set()
        [users.add(row['user']) for row in self.rows]
        return len(users)

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        users = set()
        [users.add(row['user']) for row in self.rows if row['completed'] == 'True']
        return len(users)

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        top_bite = Counter()
        for row in self.rows:
            top_bite[row['bite']] += 1
        return top_bite.most_common(1)[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        top_user = Counter()
        for row in self.rows:
            if row['completed'] == 'True':
                top_user[row['user']] += 1
        return top_user.most_common(1)[0][0]



if __name__ == '__main__':
    bites = BiteStats()
    print(bites.top_bite_by_number_of_clicks)