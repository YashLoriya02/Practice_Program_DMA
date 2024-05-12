import numpy as np
import pandas as pd

df = pd.read_csv('exp3.csv')

categories = df['Category'].unique()

ohe = np.zeros((df.shape[0], len(categories)))

for i, row in df.iterrows():
    index = np.where(categories == row['Category'])[0][0]
    ohe[i, index] = 1

print(ohe)
