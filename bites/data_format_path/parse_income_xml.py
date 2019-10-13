from pathlib import Path
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET
from collections import defaultdict

# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    tree = ET.parse(countries)
    root = tree.getroot()
    income_levels = defaultdict(list)
    for child in root:
        income_levels[child.find('{http://www.worldbank.org}incomeLevel').text].append(child.find('{http://www.worldbank.org}name').text)
    print(income_levels)


if __name__ == "__main__":
    get_income_distribution()