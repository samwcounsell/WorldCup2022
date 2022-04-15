from functions.qualifying_functions import qualifiers, icp

def complete_qualifiers(data):

    qualified, qualified_icp = qualifiers(data)
    icp_winners = icp(data, qualified_icp)

    wc_teams = ["Qatar"] + qualified + icp_winners
    print(f"\nQualified for the World Cup: {', '.join(wc_teams)}")

    return data, wc_teams

