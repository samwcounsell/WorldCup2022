from functions.group_stage import group_stage
from functions.progression import progression
from functions.knockout import knockout
from functions.worldcup_functions import knockout_fixture_list


def worldcup_finals(data, teams, sim_info):

    
    # TODO: If detailed sim make press any button to continue (do it in function)

    # Group Stage
    print("\nWelcome to the World Cup Group Stage")

    # Recording how many group stages each country achieves
    # TODO: Move into functions
    data[0].loc[data[0]['Country'].isin(teams), 'WCGS'] = data[0].loc[
                                                                      data[0]['Country'].isin(teams), 'WCGS'] + 1

    # sim_data, teams, legs, sim_type, WC, group number, group size
    groups = group_stage(data, teams, 1, sim_info, 1, 8, 4)
    qualified_ro16, null = progression(groups, 16, 0)
    print(f"\nQualified for the RO16: {', '.join(qualified_ro16)}")

    # Re-order teams
    order = [0, 3, 4, 7, 8, 11, 12, 15, 2, 1, 6, 5, 10, 9, 14, 13]
    qualified_ro16 = [qualified_ro16[i] for i in order]

    # TODO: Move into functions
    data[0].loc[data[0]['Country'].isin(qualified_ro16), 'WCR16'] = data[0].loc[
                                                              data[0]['Country'].isin(qualified_ro16), 'WCR16'] + 1

    print("\nWelcome to the World Cup RO16")
    if sim_info[0] == 0:
        knockout_fixture_list(qualified_ro16)
    qualified_qf = knockout(data, qualified_ro16, 1, sim_info, 1)
    print(f"\nQualified for the World Cup QF: {', '.join(qualified_qf)}")

    # TODO: Move into functions
    data[0].loc[data[0]['Country'].isin(qualified_qf), 'WCR8'] = data[0].loc[
                                                                        data[0]['Country'].isin(
                                                                            qualified_qf), 'WCR8'] + 1

    print("\nWelcome to the World Cup QF")
    if sim_info[0] == 0:
        knockout_fixture_list(qualified_qf)
    qualified_sf = knockout(data, qualified_qf, 1, sim_info, 1)
    print(f"\nQualified for the World Cup SF: {', '.join(qualified_sf)}")

    # TODO: Move into functions
    data[0].loc[data[0]['Country'].isin(qualified_sf), 'WCR4'] = data[0].loc[
                                                                        data[0]['Country'].isin(
                                                                            qualified_sf), 'WCR4'] + 1

    print("\nWelcome to the World Cup SF")
    if sim_info[0] == 0:
        knockout_fixture_list(qualified_sf)
    qualified_f = knockout(data, qualified_sf, 1, sim_info, 1)
    print(f"\nQualified for the World Cup Final: {', '.join(qualified_f)}")

    # TODO: Move into functions
    data[0].loc[data[0]['Country'].isin(qualified_f), 'WCF'] = data[0].loc[
                                                                        data[0]['Country'].isin(
                                                                            qualified_f), 'WCF'] + 1

    print("\nWelcome to the World Cup Final")
    if sim_info[0] == 0:
        knockout_fixture_list(qualified_f)
    winner = knockout(data, qualified_f, 2, sim_info, 1)

    # TODO: Move into functions
    data[0].loc[data[0]['Country'].isin(winner), 'WC_Wins'] = data[0].loc[
                                                                        data[0]['Country'].isin(
                                                                            winner), 'WC_Wins'] + 1

    print(f"\nThe winner of the World Cup is {winner[0]}")

    return data
