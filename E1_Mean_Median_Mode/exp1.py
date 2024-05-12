import numpy as np 
import pandas as pd 
from scipy.stats import mode 

file_path = "1_Data.csv" 
df = pd.read_csv(file_path) 

column = ["Age", "Salary"] 

for i in column: 
    current_data = df[i] 

    data_numeric = np.array(current_data)
    mean_value = np.nanmean(data_numeric) 
    median_value = np.nanmedian(data_numeric) 
    mode_value = mode(data_numeric) 
    quartiles = np.nanpercentile(data_numeric, [25, 50, 75]) 
    std_dev = np.nanstd(data_numeric) 

    print(i) 
    print("Mean : ", round(mean_value, 4)) 
    print("Median : ", round(median_value, 4)) 
    print("Mode : ", round(mode_value[0], 4)) 
    print("Std_dev : ", round(std_dev, 4)) 
    print("First Quartile (Q1):", round(quartiles[0], 4)) 
    print("Second Quartile (Q2 or Median):", round(quartiles[1], 4)) 
    print("Third Quartile (Q3):", round(quartiles[2], 4))
    print() 