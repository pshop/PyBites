#https://codechalleng.es/bites/111/
import requests
import json
from pprint import pprint

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    r = requests.get(IPINFO_URL.format(ip = ip_address))
    return r.json()['coutry']



if __name__ == '__main__':
    get_ip_country('31.164.1.149')