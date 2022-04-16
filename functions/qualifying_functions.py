from confederations.afc import afc
from confederations.caf import caf
from confederations.concacaf import concacaf
from confederations.conmebol import conmebol
from confederations.ofc import ofc
from confederations.uefa import uefa

from functions.knockout import knockout

import pandas as pd

# TODO: Inside each confederation make sure sort by World Rank before initial stages

def qualifiers(data, sim_info):

    afc_qual, afc_icp = afc(data, sim_info)
    caf_qual = caf(data, sim_info)
    conc_qual, conc_icp = concacaf(data, sim_info)
    conm_qual, conm_icp = conmebol(data, sim_info)
    ofc_icp = ofc(data, sim_info)
    uefa_qual = uefa(data, sim_info)

    qualified = afc_qual + caf_qual + conc_qual + conm_qual + uefa_qual
    icp = afc_icp + conc_icp + conm_icp + ofc_icp

    return qualified, icp


def icp(data, icp, sim_info):

    print("\nWelcome to the Inter-Continental Play Off")
    icp_winners = knockout(data, icp, 2, sim_info, 0)
    print(f"\nQualified for the World Cup: {', '.join(icp_winners)}")

    return icp_winners



