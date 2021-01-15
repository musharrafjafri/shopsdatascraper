import pandas as pd
from _collections import defaultdict


my_dict = defaultdict(list)
pd.DataFrame(my_dict, columns=['First', 'Second', 'Third']).to_csv('test.csv', mode='a')
index_num = 0
flage = True
while flage:
    for i in range(1, 6):
        index_num += 1
        my_dict['First_value'].append(i * 1000)
        if i == 4:
            flage = False
    for i in range(1, 6):
        my_dict['Second_value'].append(i * 1000)
        if i == 4:
            flage = False
    for i in range(1, 6):
        my_dict['Third_value'].append(i * 1000)
        if i == 4:
            flage = False
    form = pd.DataFrame(my_dict, index=range(1, (len(my_dict['First_value']) + 1)))
    form.to_csv('test.csv', mode='a', header=False)
for i in range(len(my_dict['First_value'])):
    print(i)
print('Keys', len(my_dict['First_value']))
# form = pd.DataFrame(my_dict, index=range(1, (len(my_dict['First_value']) + 1)))

print(index_num)
print(form)
# greet.to_csv('test4.csv', mode='a', header=False)
