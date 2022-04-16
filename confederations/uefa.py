from functions.presentation_functions import confederation_introduction, confederation_awards
from functions.group_stage import group_stage
from functions.progression import progression
from functions.knockout import knockout


def uefa(data, sim_info):

    # TODO: Add if loop for running more than one simulation

    confederation_introduction("UEFA", data)

    # TODO: Tidy this bit up
    nation_df = data[0]
    teams = nation_df.loc[nation_df['Confederation'] == 'UEFA']['Country'].to_list()

    # Round 1
    print("\nWelcome to UEFA Qualifying Round 1")
    # data, teams, legs, sim, WC, group number, group size
    groups = group_stage(data, teams, 2, sim_info, 0, 10, 6)
    qualified_a, qualified_b = progression(groups, 10, 10)

    print(f"\nQualified for the World Cup: {', '.join(qualified_a)}")
    print(f"\nQualified for Round 2: {', '.join(qualified_b)}")

    # Round 2
    print("\nWelcome to UEFA Qualifying Round 2")
    # data, teams, legs, sim, WC, group number, group size
    groups = group_stage(data, qualified_b, 2, sim_info, 0, 2, 5)
    qualified_c, qualified_d = progression(groups, 2, 2)

    print(f"\nQualified for the World Cup: {', '.join(qualified_c)}")
    print(f"\nQualified for Round 3: {', '.join(qualified_d)}")

    # Round 3
    print("\nWelcome to UEFA Qualifying Round 3")
    qualified_e = knockout(data, qualified_d, 2, sim_info, 0)
    print(f"\nQualified for the World Cup: {', '.join(qualified_e)}")

    qualified_wc = qualified_a + qualified_c + qualified_e

    print(f"\nQualified for the World Cup from UEFA: {', '.join(qualified_wc)}")

    # Awards
    confederation_awards("UEFA", data)

    return qualified_wc