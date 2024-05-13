from itertools import combinations
from collections import defaultdict
import pandas as pd

min_support = 2
min_confidence = 50

df = pd.read_csv("mainData.csv")

table_list = []
table = {}

for _, row in df.iterrows():
    transaction = set(row.dropna())
    table_list.append(transaction)

for i in range(0, len(table_list)):
    table[f'T{i}'] = list(table_list[i])

length = len(table)

def mainOperation(data):
    data = sorted(data.items(), key=lambda item: item[1], reverse=True)
    data = dict(data)
    keys = []
    for key, value in data.items():
        if value < min_support:
            keys.append(key)
    for key in keys:
            del data[key]
    return data

dict1 = {i: 0 for i in range(1, 6)}
for values in table.values():
    for value in values:
        dict1[value] += 1
dict1 = mainOperation(dict1)

combos = list(combinations(dict1.keys(), 2))
dict2 = defaultdict(int)
for combo in combos:
    for value in table.values():
        if set(combo).issubset(set(value)):
            dict2[combo] += 1
dict2 = mainOperation(dict2)

combos = list(combinations(dict1.keys(), 3))
dict3 = defaultdict(int)
for combo in combos:
    for value in table.values():
        if set(combo).issubset(set(value)):
            dict3[combo] += 1
dict3 = mainOperation(dict3)

dict1.update(dict2)
dict1.update(dict3)
main_dict = dict1

finalList = list(dict3.keys())

output = {}
c = 0
for tuples in finalList:
    new_var = []
    for i in range(0, len(finalList[c])):
        new_var.append(finalList[c][i])
    new_var += list(combinations(finalList[c], 2))
    for l in new_var:
        equation = round( ( ( ( dict3[tuples]/length) / (main_dict[l]/length ) ) * 100 ), 2 )
        output[l] = equation
    c += 1

for key,value in output.items():
    if value < min_confidence:
        print(f'{key} --> {value} --> Rejected')
    else:
        print(f'{key} --> {value} --> Accepted')
