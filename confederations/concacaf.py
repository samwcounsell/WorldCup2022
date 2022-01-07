# from functions.stage_functions import group_stage, knockout
from functions.presentation_functions import confederation_introduction

# proof of concept
import pandas as pd

player_data, nation_data = pd.read_csv('../functions/test.csv'), pd.read_csv('../functions/test.csv')
data = [player_data, nation_data]

def concacaf():

    # TODO: Add if loop for if we are running more than one simulation

    confederation_introduction("CONCACAF", data)

    #group_stage()

    #group_stage()

    #knockout()

    #return

concacaf()