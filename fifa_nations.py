import pandas as pd
from auto_batch import batch

data = pd.read_csv('fifa19_player_data.csv')
group = data.Nationality

batch(data,group)