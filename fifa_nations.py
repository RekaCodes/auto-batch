import os
import pandas as pd 

data = pd.read_csv('data.csv')
data.drop(columns={'Unnamed: 0'}, inplace=True)
data.set_index('Nationality', inplace=True)


os.mkdir('./export')


for i in data.index.unique():
    data[data.index==i].to_csv('export/'+i+'.csv')

