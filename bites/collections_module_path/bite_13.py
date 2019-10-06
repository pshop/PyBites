from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    blog_tuple = namedtuple('Blog', sorted(blog))
    return blog_tuple(**blog)



def nt2json(nt):
    blog_dict = dict()
    for field in nt._fields:
        blog_dict[field] = nt._asdict()[field]
    return json.dumps(blog_dict, indent=4, sort_keys=True, default=str)

if __name__ == '__main__':
    print(nt2json(dict2nt(blog)))