# https://codechalleng.es/bites/18/

import os
import urllib.request
from collections import Counter
import re

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    word_counter = Counter()

    with open(harry_text) as harry, open(stopwords_file) as stopwords:

        text = harry.read()
        stopwords = stopwords.read().splitlines()

        for word in re.findall(r"[\w']+", text.lower()):
            if word not in stopwords:
                word_counter[word] += 1
    return word_counter.most_common(1)[0]
            

if __name__ == '__main__':
    print(get_harry_most_common_word())