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
        self.geometry = self.features_frame['geometry']
        self.properties = self.features_frame['properties']

    def render_frame(self):
        features_frame = pd.DataFrame(self.features)
        features_frame = features_frame.drop(columns='type')

        properties_frame = pd.DataFrame()
        property_keys = []

        rendered_frame = pd.DataFrame()

        rendered_frame['coordinates'] = self.geometry.apply(lambda x: x['coordinates'])

        for key in self.properties:
            try:
                properties_frame[key] = self.properties.apply(lambda x: x[key])

            except KeyError:
                properties_frame[key] = "This is a key error"
                print("\nKey Error\n")

        rendered_frame = rendered_frame.join(properties_frame)

        return rendered_frame
