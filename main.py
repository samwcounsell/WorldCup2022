from stages.qualifying import complete_qualifiers
from stages.finals import worldcup_finals

import pandas as pd

nation_data, player_data = pd.read_csv('data/nation_data.csv'), pd.read_csv('data/player_data.csv')
data = [nation_data, player_data]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data, wc_teams = complete_qualifiers(data)

data = worldcup_finals(data, wc_teams)



