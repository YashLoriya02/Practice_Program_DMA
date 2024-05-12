from sklearn.preprocessing import OneHotEncoder
import pandas as pd

data = pd.read_csv('exp3.csv')

categorical_column = ['Category']
numerical_column = ['Count'] 

encoder = OneHotEncoder(handle_unknown='ignore') 
encoded_data = encoder.fit_transform(data[categorical_column]).toarray()
data = pd.concat([data[numerical_column], pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out())], axis=1) 

print(data)
