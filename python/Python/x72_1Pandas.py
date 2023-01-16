import pandas as pd

# df=pd.read_csv('data.csv')
# df.drop([0,2],inplace=True)
# df.drop(colums=['id'])
# print(df)


# df=pd.read_csv('id.csv')
# print(df[['Avg']].sum())
# print(df[['Avg']].min())
# print(df[['Avg']].max())


# data = [
#     [1, 'amix', 40],
#     [1, 'mixar', 25],
#     [1, 'hishas', 12],
#     [2, 'sonia', 29],
#     [2, 'mixar', 75],
#     [2, 'askips', 32],
#     [1, 'hishas', 12],
#     [2, 'sonia', 2],
#     [1, 'mixar', 7],
#     [2, 'askips', 3]
# ]

# df = pd.DataFrame(data, columns=['Code', 'Name', 'Age'])
# print("df=pd.DataFrame(data, columns=['Code','Name','Age'])      print(df) ")
# print(df)
# print("print(df[['Age']].sum())")
# print(df[['Age']].sum())
# print("print(df.groupby(['Code']).sum('Age')):   ")
# print(df.groupby(['Code']).sum('Age'))
# print("print('print(df.groupby(['Name']).min('Age')):   '')   :")
# print(df.groupby(['Name']).min('Age'))

# df = pd.read_csv('data.csv')
# print(df.axes)


# data = {
#     'name': ['amix', 'hishas', 'sonia', 'mixar', 'askips'],
#     'age': [10, 20, 30, 40, 10]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df[['age']].mean())
# print(100*'-')
# print(df[['age']].median())
# print(100*'-')
# print(df[['age']].mode())




df=pd.read_json('data.json')
print(df.to_string())