import pandas as pd
import time
import photonlib

rows_per_query = 6000
time_per_batch = 40
biz_names = photonlib.load_biznames()
data_sink = pd.DataFrame()

for biz in biz_names:
    response = photonlib.BlockObject(biz, rows_per_query).render_frame()

    data_sink = pd.concat([data_sink, response], ignore_index=True, sort=True)

    print(
        'Finished batch of {:d} for {:s}. {:d} records/{:d} categories total.\nWaiting {:d} seconds before next batch.'.format(
            rows_per_query,
            biz,
            data_sink.shape[0],
            data_sink.shape[1],
            time_per_batch
        ))

    time.sleep(time_per_batch)

data_sink.to_csv('output.csv')
