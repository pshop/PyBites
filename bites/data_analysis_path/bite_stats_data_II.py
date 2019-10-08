import csv
import re
from pathlib import Path
from urllib.request import urlretrieve
from collections import Counter

tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats) as f:
        csv_file = csv.reader(f, delimiter=';')
        bites_difficulty = Counter()

        for index, row in enumerate(csv_file):
            if index > 0 and row[1] != 'None':
                bite_index = re.findall(r"(?<=Bite )(.*)(?=\. )", row[0])[0]
                bites_difficulty[bite_index] += float(row[1])

    return [bite[0] for bite in bites_difficulty.most_common(N)]

if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)