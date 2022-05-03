import numpy as np

def post_data_update(data):

    # Updating nation sim_data
    data[0]['GFPG'] = data[0]['GF'] / data[0]['P']
    data[0]['GAPG'] = data[0]['GA'] / data[0]['P']
    data[0]['CS%'] = data[0]['Clean_Sheets'] / data[0]['P']
    data[0]['WC_GFPG'] = data[0]['WC_GF'] / data[0]['WC_P']
    data[0]['WC_GAPG'] = data[0]['WC_GA'] / data[0]['WC_P']

    # Updating player sim_data
    data[1]['GPG'] = data[1]['Goals'] / data[1]['P']
    data[1]['APG'] = data[1]['Assists'] / data[1]['P']
    data[1]['WC_GPG'] = data[1]['WC_Goals'] / data[1]['WC_P']
    data[1]['WC_APG'] = data[1]['WC_Assists'] / data[1]['WC_P']

    data[0].replace(np.inf, 0)
    data[1].replace(np.inf, 0)

    return data
