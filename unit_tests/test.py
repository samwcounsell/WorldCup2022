import pandas as pd

x = 2
teams = ['Sam', 'Keane', 'Mike']
teams2 = ['C', 'D', 'E']

a = b = pd.DataFrame(0, index=teams, columns=['P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'])
c = d = pd.DataFrame(0, index=teams2, columns=['P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'])
groups = [a, b, c, d]
print(groups[1])

qualified_a = []

for i in range(len(groups)):
    idx = groups[i].index.to_list()
    print(idx)
    qualified_a.extend(idx[0:x])
    print(qualified_a)

print(qualified_a)
