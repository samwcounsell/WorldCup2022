from functions.presentation_functions import confederation_introduction, confederation_awards
from functions.group_stage import group_stage
from functions.progression import progression
from functions.knockout import knockout


def concacaf(data, sim_info):

    # TODO: Add if loop for running more than one simulation

    confederation_introduction("CONCACAF", data)

    # TODO: Tidy this bit up
    nation_df = data[0]
    teams = nation_df.loc[nation_df['Confederation'] == 'CONCACAF']['Country'].to_list()

    # Round 1
    print("\nWelcome to CONCACAF Qualifying Round 1")
    groups = group_stage(data, teams[5:], 2, sim_info, 0, 6, 5)
    qualified_a, null = progression(groups, 6, 0)
    print(f"\nQualified: {', '.join(qualified_a)}")

    # Round 2
    print("\nWelcome to CONCACAF Qualifying Round 2")
    qualified_b = knockout(data, qualified_a, 2, sim_info, 0)
    print(f"\nQualified: {', '.join(qualified_b)}")

    teams = teams[:5]
    teams.extend(qualified_b)

    # Round 3
    print("\nWelcome to AFC Qualifying Round 3")
    groups = group_stage(data, teams, 2, sim_info, 0, 1, len(teams))
    qualified_wc, qualified_icp = progression(groups, 3, 1)

    print(f"\nQualified for the World Cup: {', '.join(qualified_wc)}")
    print(f"\nQualified for the Inter-Continental Play Off: {', '.join(qualified_icp)}")

    # Awards
    confederation_awards("CONCACAF", data)

    return qualified_wc, qualified_icp