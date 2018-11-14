import pandas as pd
import numpy as np
import photonlib
import json
from pandas.io.json import json_normalize

rows_per_query = 2
biz_names = photonlib.load_biznames()
data_sink = pd.DataFrame()

# for biz in biz_names:

query_json = photonlib.get_data(query='Walmart', num_items=rows_per_query)

line_name = query_json.get('features', {'properties'})




print(print(query_json))
'''
result = {
    'name': query_list['properties'].get('name')
}

print(result)
'''

# df = pd.DataFrame.from_records(query_list, index=None)

