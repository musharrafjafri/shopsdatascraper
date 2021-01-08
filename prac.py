import pandas as pd
from _collections import defaultdict
import Files
my_dict = defaultdict(list)

for i in range(5):
    my_dict['First'].append(i)

for j in range(5):
    my_dict['Second'].append(j)

print(len(my_dict['First']) + 1)
form = pd.DataFrame(my_dict, index=range(1, (len(my_dict['First']) + 1)))
print(form)

# form.to_csv('test1.csv', index=False)