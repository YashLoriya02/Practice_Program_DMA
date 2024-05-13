import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("5_age_bmi.csv")

q1 = np.percentile(df["Age"], 25)
q3 = np.percentile(df["Age"], 75)
iqr = q3-q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = (df["Age"] < lower_bound) | (df["Age"] > upper_bound)
filtered_data = df["Age"][~outliers]

print("Filtered Data:")
print(filtered_data)

plt.boxplot([df["Age"], filtered_data], labels=['Original Data', 'Filtered Data'])
plt.xlabel('Data')
plt.ylabel('Values')
plt.title('Box Plot of Age and BMI')
plt.show()

plt.scatter(df["Age"], df["BMI"])
plt.xlabel('Age')
plt.ylabel('BMI')
plt.title('Scatter Plot of Age and BMI')
plt.show()
