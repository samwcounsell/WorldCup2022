def welcome():

    print("\nWelcome to the Python World Cup 2022 by samwcounsella and githubkeano!")

def confederation_introduction(confederation, data):

    print(f"\nWelcome to the {confederation} World Cup qualifying section;")

    # Pulling nation sim_data from the sim_data list, then selecting only nations from that confederation and sorting
    nation_df = data[0]
    df = nation_df.loc[nation_df['Confederation'] == confederation].sort_values(by=['World Rank']).reset_index()

    # Printing top three favourites (by World Rank) to qualify for the World Rank
    print(f"\nThe favourites to qualify for the World Cup are {', '.join(df.loc[0:1]['Country'].to_list())} and {df.loc[2]['Country']}")


def confederation_awards(confederation, data, sim_info):

    confederation_df = data[1].loc[data[1]['Confederation'] == confederation]

    goal_df = confederation_df.sort_values(by=['Goals', 'P', 'Assists'], ascending = [False, True, False]).reset_index()
    assist_df = confederation_df.sort_values(by=['Assists', 'P', 'Goals'], ascending = [False, True, False]).reset_index()

    print(f"\nThe top goalscorer is {goal_df.loc[0]['Name']} with {goal_df.loc[0]['Goals']} goals in {goal_df.loc[0]['P']} games.")
    print(f"\nThe top playmaker is {assist_df.loc[0]['Name']} with {assist_df.loc[0]['Assists']} assists in {assist_df.loc[0]['P']} games.")

    if sim_info[0] == 0:
        input("\nPress any button to continue: ")