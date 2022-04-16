from functions.qualifying_functions import qualifiers, icp

def complete_qualifiers(data, sim_info):

    qualified, qualified_icp = qualifiers(data, sim_info)
    icp_winners = icp(data, qualified_icp, sim_info)

    wc_teams = ["Qatar"] + qualified + icp_winners
    print(f"\nQualified for the World Cup: {', '.join(wc_teams)}")

    return data, wc_teams

