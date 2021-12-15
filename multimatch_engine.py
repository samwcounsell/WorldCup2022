from scipy.stats import binom

# Gives probability each team scores with every Bernoulli trial (each minute)
p_home, p_away = 0.014, 0.014

def multimatch(p_home, p_away):

    # Running binomial simulation with size 90
    score_home, score_away = binom.rvs(90, p_home), binom.rvs(90, p_away)

    # Printing the match result (Replace this with post_match later)
    print(f"\nFinal Score: {score_home} - {score_away}")

multimatch(p_home, p_away)