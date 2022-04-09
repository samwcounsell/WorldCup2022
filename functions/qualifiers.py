from confederations.afc import afc
from confederations.caf import caf
from confederations.concacaf import concacaf
from confederations.conmebol import conmebol
from confederations.ofc import ofc
from confederations.uefa import uefa

from functions.knockout import knockout

import pandas as pd

nation_data, player_data = pd.read_csv('../data/nation_data.csv'), pd.read_csv('../data/player_data.csv')
data = [nation_data, player_data]


def complete_qualifiers(data):

    qualified, qualified_icp = qualifiers(data)
    icp_winners = icp(data, qualified_icp)

    wc_teams = ["Qatar"] + qualified + icp_winners
    print(f"\nQualified for the World Cup: {', '.join(wc_teams)}")
    print(len(wc_teams))

    return wc_teams


# TODO: Inside each confederation make sure sort by World Rank before initial stages

def qualifiers(data):

    afc_qual, afc_icp = afc(data)
    caf_qual = caf(data)
    conc_qual, conc_icp = concacaf(data)
    conm_qual, conm_icp = conmebol(data)
    ofc_icp = ofc(data)
    uefa_qual = uefa(data)

    qualified = afc_qual + caf_qual + conc_qual + conm_qual + uefa_qual
    icp = afc_icp + conc_icp + conm_icp + ofc_icp

    return qualified, icp


def icp(data, icp):

    print("\nWelcome to the Inter-Continental Play Off")
    icp_winners = knockout(data, icp, 2, 1, 0)
    print(f"\nQualified for the World Cup: {', '.join(icp_winners)}")

    return icp_winners


complete_qualifiers(data)

