import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import OneHotEncoder
import statistics as st
from scipy import stats

data = pd.read_csv("4_BSE.csv")

mean_value = data.mean(numeric_only=True) 
median_value = data.median(numeric_only=True)

numerical_cols = ['R&D Spend', 'Marketing Spend', 'Administration']
categorical_cols = ['State']

encoder = OneHotEncoder() 
encoded_data = encoder.fit_transform(data[categorical_cols]).toarray()
data = pd.concat([data[numerical_cols], pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out()), data['Profit']], axis=1) 

X = data.iloc[:, :-1].values
y = data['Profit'].values

z_scores = stats.zscore(data[['R&D Spend', 'Marketing Spend', 'Administration', 'Profit']])
outlier_indices = np.where(np.abs(z_scores) > 3)[0]
outliers = data.iloc[outlier_indices]
outliers.to_csv("outliers.csv", index=False)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0) 

print("X Train") 
print(X_train, "\n") 
print("X Test") 
print(X_test, "\n") 
print("Y Train") 
print(y_train,"\n") 
print("Y Test") 
print(y_test, "\n") 

print("Mean : ", round(mean_value, 4)) 
print("Median : ",median_value) 

train_count = len(X_train)
test_count = len(X_test) 

plt.figure() 
plt.bar('Train', train_count, color='blue', label='Train Data') 
plt.bar('Test', test_count, color='red',label='Test Data') 
plt.xlabel('Data Set') 
plt.ylabel('Number of Samples') 
plt.title('Number of Samples in Train and Test Sets') 
plt.legend() 
plt.show()
