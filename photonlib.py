import requests
import pandas as pd


def load_biznames():
    with open('Business_Names.txt', encoding='utf-8') as file:
        biz_names = [line.strip() for line in file]

    return biz_names


def url_constructor(path):
    return 'http://photon.komoot.de/api/?' + path


class BlockObject(object):

    def __init__(self, query: str, block_size: int):
        self.query = query
        self.block_size = block_size

        self.raw_data = requests.get(
            url_constructor('q=\'{:s}\'&limit={:d}'.format(self.query, self.block_size))).json()
        self.features = self.raw_data['features']
        self.features_frame = pd.DataFrame(self.features)

    def render_frame(self):

        feature_frame = pd.DataFrame(self.features)

        rendered_frame = pd.concat((pd.DataFrame(feature_frame[col].values.tolist()) for col in feature_frame), axis=1)

        rendered_frame = rendered_frame.drop(columns=[ 'osm_id', 'osm_type', 'osm_value', 'type'])

        return rendered_frame
