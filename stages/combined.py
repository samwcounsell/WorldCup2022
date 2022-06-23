from stages.qualifying import complete_qualifiers
from stages.finals import worldcup_finals

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def worldcup_simulation(data, sim_info, sim_num):

    complete_nation_data, complete_player_data = pd.read_csv('sim_data/complete_nation_data.csv'), pd.read_csv(
        'sim_data/complete_player_data.csv')

    for i in range(sim_num):

        data, wc_teams = complete_qualifiers(data, sim_info)

        # TODO: Actually stop people putting in non numbers without error as is done at start
        if sim_info[0] == 0:
            sim_info[1] = float(input('Choose delay for World Cup Finals: '))

        data = worldcup_finals(data, wc_teams, sim_info)

        # TODO: move to function later
        # Data merging
        nation_sum_cols = ['P', 'GF', 'GA', 'Clean_Sheets', 'WC_P', 'WC_GF', 'WC_GA', 'WCGS', 'WCR16', 'WCR8', 'WCR4', 'WCF', 'WC_Wins']
        for j in range(len(nation_sum_cols)):
            complete_nation_data[nation_sum_cols[j]] = complete_nation_data[nation_sum_cols[j]] + data[0][
                nation_sum_cols[j]]
            data[0][nation_sum_cols[j]] = 0

        player_sum_cols = ['P', 'Goals', 'Assists', 'WC_P', 'WC_Goals', 'WC_Assists']
        for j in range(len(player_sum_cols)):
            complete_player_data[player_sum_cols[j]] = complete_player_data[player_sum_cols[j]] + data[1][
                player_sum_cols[j]]
            data[1][player_sum_cols[j]] = 0

    complete_data = [complete_nation_data, complete_player_data]

    return complete_data
