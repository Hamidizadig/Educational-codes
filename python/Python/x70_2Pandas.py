import pandas as pd

# df=pd.read_csv('data.csv')
# print(df)
# print(df.tostring())
# print(df[['Name','Family']].iloc[0])
# print(df.head(3))
# print(df.tail(3))
# print(df.info())
# new_df=df.rename(columns={'id':'IIIIIIIIIIIIIIIIIIIIIIII','date':'DDDDDDDDDDDDDDDDDDDDDD'})
# print(df)
# print(100*'-')
# print(new_df)


df = pd.read_csv('data.csv')
df.rename(columns={'id': 'IIIIIIIIIIIIIIIIIIIIIIII',
          'date': 'DDDDDDDDDDDDDDDDDDDDDD'}, inplace=True)
print(df)
