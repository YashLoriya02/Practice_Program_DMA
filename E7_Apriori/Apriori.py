from itertools import combinations
from collections import defaultdict

min_support = 2
min_confidence = 50

table = {
    "T1" : [1,2,5],
    "T2" : [2,4],
    "T3" : [2,3],
    "T4" : [1,2,4],
    "T5" : [1,3],
    "T6" : [2,3],
    "T7" : [1,3],
    "T8" : [1,2,3,5],
    "T9" : [1,2,3]
}

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
