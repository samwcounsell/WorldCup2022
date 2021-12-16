from scipy.stats import binom

# multi_sim_match runs the whole match as part of multiple World Cup simulations
def multi_sim_match(home, away):

    # run match_data_retrieval here
        # import not required
        # return p_home, p_away, player_lists and their ratings

    # Running binomial simulation with size 90
    score_home, score_away = binom.rvs(90, p_home), binom.rvs(90, p_away)

    # Printing the match result (Replace this with post_match later)
    print(f"\nFinal Score: {score_home} - {score_away}")


# calculates detail of main events i.e., goals for a multi_sim_match
def multi_sim_events():

    # Calculate goalscorers
    # Calculate assisters

# Variable Glossary
# home/away - the two teams playing the match
# p_home/p_away - probability of home/away team scoring each minute
# score_home/score away - number of goals scored in the match by home/away team