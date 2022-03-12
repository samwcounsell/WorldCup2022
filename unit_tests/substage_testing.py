from functions.substage_functions import group_draw, group_simulation

import pandas as pd

df = pd.read_csv('test.csv')
list = df.loc[df['Confederation'] == 'UEFA']['Country'].to_list()

group_draw(11, 4, list)

group_simulation(list[:8], 2)