import pandas as pd

df = pd.read_csv('data.csv')
# print(df.to_string())

# new_df=df.dropna()
# print(new_df.to_string())


# new_df=df.fillna('OOOOO')
# print(new_df.to_string())

# new_df=df[['Avg']].fillna({'id':'NO ID' ,'link':'NO LINK'})
# print(new_df.to_string())

for index in df.index:
    if df.loc[index, 'id'] < 10 or df.loc[index, 'id'] > 10000000000000:
        df.loc[index, 'id'] = 0

print(df.to_string())

df.drop_duplicated(inplace=True)
print(df.to_string())
