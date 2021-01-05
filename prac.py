from _collections import defaultdict
import pandas as pd

my_dict = defaultdict(list)
for i in range(4):
    my_dict['Name'].append(i)
for i in range(4):
    my_dict['CNo'].append(i)
for i in range(4):
    my_dict['Adress'].append(i)
print(my_dict.values())

data_f = pd.DataFrame(my_dict)
print(data_f)