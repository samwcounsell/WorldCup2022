import random, time, pandas as pd


def worldcup_draw(data, teams, sim_info):

    # Ordering the teams
    df = data[0].loc[data[0]['Country'].isin(teams)][['Country', 'Confederation', 'World Rank']].sort_values('World Rank')
    qatar = df.loc[df['Country'] == 'Qatar']
    df = df[df['Country'] != 'Qatar']
    df = pd.concat([qatar, df]).reset_index(drop=True)

    # First team in each group
    groups = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H']

    if sim_info[0] == 0:
        time.sleep(sim_info[1] * 10)
        print("\nPot 1")

    for i in range(8):

        groups[i] = df.iloc[i: i + 1]

        if sim_info[0] == 0:
            time.sleep(sim_info[1] * 10)
            print(f"\n{groups[i].to_string(index = False)}")

    # Teams 2 onwards
    for j in range(1, 4):

        if sim_info[0] == 0:
            time.sleep(sim_info[1] * 10)
            print(f"\nPot {j + 1}")

        if j == 1:
            df_2 = df[8 * j: 8 * j + 8].sort_values('Confederation', ascending = False).reset_index(drop = True)
        if j == 2:
            df_2 = df[8 * j: 8 * j + 8].sort_values('Confederation', ascending = True).reset_index(drop = True)
        if j == 3:
            df_2 = df[8 * j: 8 * j + 8].sort_values('Confederation', ascending = False).reset_index(drop = True)

        complete = 0
        unassigned = list(range(8))

        while complete == 0:

            try:

                for i in range(8):

                    attempt = 0
                    drawn = 0
                    drawn_team, drawn_team_conf = df_2.iloc[i: i + 1], df_2.loc[i, 'Confederation']

                    while drawn == 0:

                        x = unassigned[attempt]

                        existing_conf = groups[x]["Confederation"].to_list()

                        if (drawn_team_conf == 'UEFA' and existing_conf.count(
                                drawn_team_conf) < 2) or existing_conf.count(
                                drawn_team_conf) == 0:

                            # groups[x] = groups[x].append(drawn_team, ignore_index=True)
                            groups[x] = pd.concat([groups[x], drawn_team])
                            drawn = 1

                            if sim_info[0] == 0:
                                time.sleep(sim_info[1] * 10)
                                print(f"\n{groups[x].to_string(index = False)}")

                            if i == 7:
                                complete = 1
                                break

                            del unassigned[attempt]

                        else:
                            attempt = attempt + 1

                break


            except:

                if complete == 0:
                    unassigned = [0, 1, 2, 3, 4, 5, 6, 7]
                    random.shuffle(unassigned)

                    for k in range(8):
                        groups[k] = groups[k].head(j)

                continue

    for i in range(8):

        groups[i] = groups[i]['Country'].to_list()

    return groups


