import pandas as pd
import numpy as np
import statistics as st

df = pd.read_csv("2_DMAL.csv")

print()
print("Count of Null Values in each row:")
print(df.isnull().sum())
print()

drop = df.dropna()
print("Dataframe without rows of null values:")
print(drop)
print()

fill = df.fillna(10)
print("Dataframe with null values filled as 10:")
print(fill)
print()

# fill_back = df.fillna(method='bfill', axis=0)  -------> Deprecated
fill_backward = df.bfill()
print("Dataframe with null values filled as Forward Value:")
print(fill_backward)
print()

# fill_forw = df.fillna(method='ffill')  -------> Deprecated
fill_forward = df.ffill()
print("Dataframe with null values filled as Backward Value:")
print(fill_forward)
print()

rep= df.replace(21, 35)
print("Dataframe with value 21 replaced with 35:")
print(rep)
print()

mean = df.mean(numeric_only=True)
rep_mean=df.replace(to_replace=np.nan, value=mean)
print("Dataframe with NaN filled with mean:")
print(rep_mean)
print()

med = df.median(numeric_only=True)
rep_med=df.replace(to_replace=np.nan, value=med)
print("Dataframe with NaN filled with median:")
print(rep_med)
print()

mode = st.mode(df.select_dtypes(include=np.number).stack())
rep_mode = df.replace(to_replace=np.nan, value=mode)
print("Dataframe with NaN filled with mode:")
print(rep_mode)
print()

print("Dataframe with NaN filled by using InterPolation:")
print(df.interpolate(method ='linear', limit_direction ='forward'))
print()
