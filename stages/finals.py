from functions.group_stage import group_stage
from functions.progression import progression
from functions.knockout import knockout

def worldcup_finals(data, teams):

    # Group Stage
    print("\nWelcome to the World Cup Group Stage")
    # data, teams, legs, sim, WC, group number, group size
    groups = group_stage(data, teams, 1, 1, 1, 8, 4)
    qualified_ro16, null = progression(groups, 16, 0)
    print(f"\nQualified for the RO16: {', '.join(qualified_ro16)}")

    # Re-order teams
    order = [0, 3, 4, 7, 8, 11, 12, 15, 2, 1, 6, 5, 10, 9, 14, 13]
    qualified_ro16 = [qualified_ro16[i] for i in order]

    print("\nWelcome to the World Cup RO16")
    qualified_qf = knockout(data, qualified_ro16, 1, 1, 1)
    print(f"\nQualified for the World Cup QF: {', '.join(qualified_qf)}")

    print("\nWelcome to the World Cup QF")
    qualified_sf = knockout(data, qualified_qf, 1, 1, 1)
    print(f"\nQualified for the World Cup SF: {', '.join(qualified_sf)}")

    print("\nWelcome to the World Cup SF")
    qualified_f = knockout(data, qualified_sf, 1, 1, 1)
    print(f"\nQualified for the World Cup Final: {', '.join(qualified_f)}")

    print("\nWelcome to the World Cup Final")
    winner = knockout(data, qualified_f, 1, 1, 1)

    print(f"\nThe winner of the World Cup is {winner[0]}")

    return data
