from functions.presentation_functions import confederation_introduction, confederation_awards
from functions.group_stage import group_stage
from functions.progression import progression
from functions.knockout import knockout


def caf(data, sim_info):

    # TODO: Add if loop for running more than one simulation

    confederation_introduction("CAF", data)

    # TODO: Tidy this bit up
    nation_df = data[0]
    teams = nation_df.loc[nation_df['Confederation'] == 'CAF']['Country'].to_list()

    # Round 1
    print("\nWelcome to CAF Qualifying Round 1")
    qualified = knockout(data, teams[26:], 2, sim_info, 0)

    teams = teams[:26]
    teams.extend(qualified)

    # Round 2
    print("\nWelcome to CAF Qualifying Round 2")
    # data, teams, legs, sim, WC, group number, group size
    groups = group_stage(data, teams, 2, sim_info, 0, 10, 4)
    qualified_a, qualified_b = progression(groups, 10, 0)

    print(f"\nQualified: {', '.join(qualified_a)}")

    # Round 3
    print("\nWelcome to CAF Qualifying Round 3")
    qualified_wc = knockout(data, qualified_a, 2, sim_info, 0)

    print(f"\nQualified for the World Cup: {', '.join(qualified_wc)}")

    # Awards
    confederation_awards("CAF", data)

    return qualified_wc
