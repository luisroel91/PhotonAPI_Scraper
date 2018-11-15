import pandas as pd
import numpy as np
import photonlib
import json
from pandas.io.json import json_normalize

rows_per_query = 2
biz_names = photonlib.load_biznames()
data_sink = pd.DataFrame()

for biz in biz_names:

    query_json = photonlib.get_data(query=biz,)



