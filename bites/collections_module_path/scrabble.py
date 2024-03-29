import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as file:
        words = file.read()
    return words.split('\n')[:-1]


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    final_score = 0
    for letter in word:
        for score in scrabble_scores:
            if letter.upper() in score[1]:
                final_score += score[0]
    return final_score


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    score_list = [calc_word_value(word) for word in words]
    return words[score_list.index(max(score_list))]

if __name__ == '__main__':
    print(max_word_value(load_words()))