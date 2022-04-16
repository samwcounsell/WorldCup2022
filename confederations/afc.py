from functions.presentation_functions import confederation_introduction, confederation_awards
from functions.group_stage import group_stage
from functions.progression import progression
from functions.knockout import knockout

import pandas as pd

def afc(data, sim_info):

    # TODO: Add if loop for running more than one simulation

    confederation_introduction("AFC", data)

    # TODO: Tidy this bit up
    nation_df = data[0]
    teams = nation_df.loc[nation_df['Confederation'] == 'AFC']['Country'].to_list()
    teams.remove("Qatar")

    # Round 1
    print("\nWelcome to AFC Qualifying Round 1")
    qualified = knockout(data, teams[35:], 2, sim_info, 0)

    teams = teams[:35]
    teams.extend(qualified)

    # Round 2
    print("\nWelcome to AFC Qualifying Round 2")
    # data, teams, legs, sim, WC, group number, group size
    groups = group_stage(data, teams, 2, sim_info, 0, 8, 5)
    qualified_a, qualified_b = progression(groups, 12, 0)

    print(f"\nQualified: {', '.join(qualified_a)}")

    # Round 3
    print("\nWelcome to AFC Qualifying Round 3")
    groups = group_stage(data, qualified_a, 2, sim_info, 0, 2, 6)
    qualified_wc, qualified_c = progression(groups, 4, 2)

    print(f"\nQualified for the World Cup: {', '.join(qualified_wc)}")
    print(f"\nQualified for AFC Round 4: {', '.join(qualified_b)}")

    # Round 4
    qualified_icp = knockout(data, qualified_c, 2, sim_info, 0)

    print(f"\nQualified for the Inter-Continental Play Off: {''.join(qualified_icp)}")

    # Awards
    confederation_awards("AFC", data)

    return qualified_wc, qualified_icp
