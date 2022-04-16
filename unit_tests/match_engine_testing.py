import random

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

from scipy.stats import bernoulli

from matchengine.simple_engine import multi_sim_match

n_df = pd.DataFrame(0, index = [0, 1], columns=['Country', 'Attack', 'Defense', 'P', 'GF', 'GA', 'Clean_Sheets', 'WC_P', 'WC_GF', 'WC_GA'])
n_df['Country'] = ['Brazil', 'Japan']
n_df['Attack'] = [1.9, 1.1]
n_df['Defense'] = [1.6, 1.2]

home = 'Brazil'
away = 'Japan'

p_df = pd.DataFrame(0, index = [0, 1, 2, 3, 4, 5], columns=['Name', 'Country', 'Attack', 'Passing' ,'P', 'Goals', 'Assists' ,'WC_P','WC_Goals','WC_Assists'])
p_df['Name'] = ['Neymar', 'Santos', 'Viera', 'Ieyasu', 'Miyagi', 'Nagano']
p_df['Attack'] = [1, 10, 2, 5, 1, 10]
p_df['Passing'] = [1, 10, 2, 5, 1, 3]
p_df['Country'] = ['Brazil', 'Brazil', 'Brazil', 'Japan', 'Japan', 'Japan']

for i in range(10):
    n_df, p_df = multi_sim_match(n_df, p_df, 'Brazil', 'Japan', 'Yes')
    print(n_df)
    print()
    print(p_df)

