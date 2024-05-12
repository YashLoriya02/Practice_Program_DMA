import pandas as pd

df=pd.read_csv('exp3.csv')

en = pd.get_dummies(df, columns=['Category'])
en.replace({ False: 0, True: 1 }, inplace=True)

print(en)
