import requests
import pandas as pd
from pandas.io.json import json_normalize
import time


def load_biznames():
    with open('Business_Names.txt', encoding='utf-8') as file:
        biz_names = [line.strip() for line in file]

    return biz_names


def url_constructor(path):
    return 'http://photon.komoot.de/api/?' + path


def unpack_frame():
    pass


class BlockObject(object):

    def __init__(self, query: str, block_size: int):
        self.query = query
        self.block_size = block_size

        self.raw_data = requests.get(
            url_constructor('q=\'{:s}\'&limit={:d}'.format(
                self.query,
                self.block_size
            ))).json()

        self.features = self.raw_data['features']

    def generate_dataframe(self):
        features_frame = pd.DataFrame(self.features)
        features_frame = features_frame.drop(columns='type')

        coord_frame = features_frame['geometry'][:].loc[0]['coordinates']
        properties_frame = features_frame['properties']


        rendered_frame = pd.DataFrame()



        return coord_frame

        '''
        for counter, row in enumerate(features_frame.iterrows()):
        element_name = row

        print(element_name, counter)
        feature_coord = row['geometry'][index]['coordinates']
        feature_name = features_frame['']
        '''


response = BlockObject('Home Depot', block_size=2)
print(response.generate_dataframe())
