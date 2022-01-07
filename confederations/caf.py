# from functions.stage_functions import group_stage, knockout
from functions.presentation_functions import confederation_introduction

# proof of concept
import pandas as pd

player_data, nation_data = pd.read_csv('../functions/test.csv'), pd.read_csv('../functions/test.csv')
data = [player_data, nation_data]

def caf():

    # TODO: Add if loop for running more than one simulation

    confederation_introduction("CAF", data)

    #knockout()

    #group_stage()

    #knockout()

    #return

caf()