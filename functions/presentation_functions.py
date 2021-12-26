
def confederation_introduction(confederation, data):

    print(f"\nWelcome to the {confederation} World Cup qualifying section;")

    # Pulling nation data from the data list, then selecting only nations from that confederation and sorting
    nation_df = data[1]
    df = nation_df.loc[nation_df['Confederation'] == confederation].sort_values(by=['World Rank']).reset_index()

    # Printing top three favourites (by World Rank) to qualify for the World Rank
    print(f"\nThe favourites to qualify for the World Cup are {', '.join(df.loc[0:1]['Country'].to_list())} and {df.loc[2]['Country']}")
