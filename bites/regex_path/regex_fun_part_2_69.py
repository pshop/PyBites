# https://codechalleng.es/bites/69/

import re

def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    if re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", text) is not None:
        return True
    else:
        return False


def is_integer(number):
    """Return True if number is an integer"""
    if re.match(r"^-?\d+$", str(number)):
        return True
    else:
        return False


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    if re.search(r"\w+-\w+", text):
        return True
    return False


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    if re.search(r"\s\(.*?\)\s", text):
        return re.sub(r"\s\(.*?\)\s",' ', text)
    return re.sub(r"\s?\(.*?\)\s?", '', text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    return [word.strip() for word in re.split(r"[?!.,;]", text) if word != '']


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r" +", ' ', text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    if re.search(r"[aeiouy]{3,}", word):
        return True
    return False


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    if re.match(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", date):
        day_month = re.findall(r"[0-9]{2}", date)
        AMER_date = day_month[1]+'/'+day_month[0]+'/'+day_month[2]+day_month[3]
        return AMER_date
    return date


if __name__ == "__main__":
    convert_emea_date_to_amer_date('31/03/2018')