from functions.worldcup_functions import worldcup_draw
from stages.qualifying import complete_qualifiers
import pandas as pd

nation_data, player_data = pd.read_csv('../sim_data/nation_data.csv'), pd.read_csv('../sim_data/player_data.csv')
data = [nation_data, player_data]

for i in range(50):

    data, wc_teams = complete_qualifiers(data)

    groups = worldcup_draw(data, wc_teams)

    for j in range(8):

        print("\n", groups[j])