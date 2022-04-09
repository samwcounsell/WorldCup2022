from functions.presentation_functions import confederation_introduction, confederation_awards
from functions.group_stage import group_stage
from functions.progression import progression
from functions.knockout import knockout


def ofc(data):

    # TODO: Add if loop for running more than one simulation

    confederation_introduction("OFC", data)

    # TODO: Tidy this bit up
    nation_df = data[0]
    teams = nation_df.loc[nation_df['Confederation'] == 'OFC']['Country'].to_list()

    # Round 1
    print("\nWelcome to OFC Qualifying Round 1")
    qualified = knockout(data, teams[9:], 2, 1, 0)

    teams = teams[:9]
    teams.extend(qualified)

    # Round 2
    print("\nWelcome to OFC Qualifying Round 2")
    # data, teams, legs, sim, WC, group number, group size
    groups = group_stage(data, teams, 2, 1, 0, 2, 5)
    qualified_a, qualified_b = progression(groups, 4, 0)

    print(f"\nQualified: {', '.join(qualified_a)}")

    # Round 3
    print("\nWelcome to OFC Qualifying Round 3")
    # Reordering teams to ensure correct matchups
    order = [0, 3, 1, 2]
    qualified_a = [qualified_a[i] for i in order]
    qualified = knockout(data, qualified_a, 2, 1, 0)

    print(f"\nQualified: {', '.join(qualified)}")

    # Round 4
    print("\nWelcome to OFC Qualifying Round 4")
    qualified_icp = knockout(data, qualified, 2, 1, 0)

    print(f"\nQualified for the Inter-Continental Play Off: {''.join(qualified_icp)}")

    # Awards
    confederation_awards("OFC", data)

    return qualified_icp