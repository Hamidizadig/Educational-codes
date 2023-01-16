import pandas as pd
# print(pd.__version__)

# data=[2,4,5,4,5,7]
# ser=pd.Series(data)
# print(ser)




# data=[2,4,5,4,5,7]
# ser=pd.Series(data)
# print(ser)
# print(100*"-")

# data=[2,4,5,4,5,7]
# ser=pd.Series(data,index=['a','b','c','d','e','f'])
# print(ser)



data={
    'Red':100,
    "Blue":200,
    "Green":130,
    "Yellow":187,
}
ser=pd.Series(data)
print(ser)
print(100*"-")
print(ser['Green'])
print(ser[1])