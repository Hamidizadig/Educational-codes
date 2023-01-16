import pandas as pd

# data=[3,4,6,7,6]
# df=pd.DataFrame(data)
# print(df)


# data=[3,4,6,7]
# df=pd.DataFrame(data,index=['sorex','zisha','rifax','pofic'],columns=['Age'])
# print(df)


data={
    'Color':['Red','Green','Blue'],
    'Grade':[100,130,200],
    'Price':[1000,2000,3000],
    'size':[20,21,24]
}
df=pd.DataFrame(data,index=['a','b','c'])
print(df)