import requests
import time


def load_biznames():
    with open('Business_Names.txt', encoding='utf-8') as file:
        biz_names = [line.strip() for line in file]

    return biz_names


def get_data(query, num_items):  # Make this rate limit somehow
    data = requests.get(_url('q=\'{:s}\'&limit={:d}'.format(query, num_items)))
    data = data.json()
    time.sleep(1)
    return data


def _url(path):
    return 'http://photon.komoot.de/api/?' + path
