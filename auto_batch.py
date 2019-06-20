

def batch(data, group):
    import os
    import pandas as pd 
    
    data.set_index(group, inplace=True)
    os.mkdir('./export')


    for i in data.index.unique():
        data[data.index==i].to_csv('export/'+i+'.csv')

