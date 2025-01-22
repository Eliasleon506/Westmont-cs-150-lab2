import pandas as pd

#print("Hello, pandas!")

s = pd.Series(["c","s",1,5,0])
#print(s)

df = pd.DataFrame({"Professor": "Mike",
                   'Classes':["cs-150", "cs-030", "senior-sem"],
                   "Me": ["attending","tutor", "not yet;)" ]})

#print(df)

print(df.iloc[2,2])

df.iloc[2,2] = "Oh no I am a senior !!"

print(df)