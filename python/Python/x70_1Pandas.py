import pandas as pd

data={
    'Color':['Red','Green','Blue'],
    'Grade':[100,130,200],
    'Price':[1000,2000,3000],
    'size':[20,21,24]
}
df=pd.DataFrame(data)
print(df)
print(100*'-')
print(df.loc[0])
print(df.loc[0]['Grade'])
print(df[['Color','Price']])
print(df[['Color','Price']].loc[1])
print(df.iloc[0])

--

