# https://codechalleng.es/bites/112/

# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string(social_platforms=social_platforms):
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    sp_dict = dict()
    for platform in social_platforms.split('\n\n'):
        lines = platform.splitlines()
        range_min = int(re.findall(r"\d+", lines[1])[0])
        range_max = int(re.findall(r"\d+", lines[2])[0])
        validator = '['
        for e in lines[3].split(' ')[4:]:
          validator += e.strip()
        validator += ']+$'
        sp_dict[lines[0]] = Validator(
          range= range(range_min,range_max),
          regex=re.compile(validator))
    return sp_dict




def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    try:
      all_validators[platform]
    except:
      raise ValueError
    if all_validators[platform].regex.match(username) and\
      len(username) in all_validators[platform].range:
      return True
    return False


    

if __name__ == "__main__":
    print(validate_username('Twitter', 'pshop'))