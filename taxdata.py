import pandas as pd

data = pd.read_csv('SAMPLE_ITR/ITR3-SAMPLE_AY_2017-18.TXT', sep='|')
data.to_csv('pit.csv', index=False)
