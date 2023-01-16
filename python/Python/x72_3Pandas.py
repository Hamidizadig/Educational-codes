import pandas as pd
import matplotlib.pyplot as plt

# df=pd.read_json('data.json')
df = pd.read_csv('data.csv')
print(df)
df.plot(x='id', y='date')
plt.show()


# data = {
#     'name': ['amix', 'hishas', 'sonia', 'mixar', 'askips'],
#     'age': [10, 20, 30, 40, 10]
# }
