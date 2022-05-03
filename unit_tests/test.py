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
    groups[i] = groups[i].iloc[x:]

print(qualified_a)
print(groups[2])

df = pd.DataFrame(columns=['P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'])
df = pd.concat([df, c.head(1), a.head(1)])
print(df)


# DASH CODE
fig3 = go.Figure(
    data=[
        go.Bar(
            name="Original",
            x=data["Country"],
            y=data["WCGS"],
            offsetgroup=0,
        ),
        go.Bar(
            name="Model 1",
            x=data["Country"],
            y=data["WCR16"],
            offsetgroup=0,
        )
    ],
    layout=go.Layout(
        title="Issue Types - Original and Models",
        yaxis_title="Number of Issues",
        font=dict(
            family="Courier New, monospace",
            size=8,
            color="RebeccaPurple"
        )
    )
)
