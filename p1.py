
import pandas as pd

#table_df=pd.read_csv('http://www.it.uc3m.es/alberto/AI/193.242.98.141.table.20210121.1600_first100', delimiter='|')
table_df=pd.read_csv('http://www.it.uc3m.es/alberto/AI/193.242.98.141.table.20210121.1600.gz', delimiter='|')

unique_pref = table_df['destination_prefix'].unique()

pref = table_df['destination_prefix']

total_length = len(pref)

unique_length = len(unique_pref)

rep = total_length - unique_length

print(total_length)

print(rep)


AS_path_df = table_df['as_path']

print(len(AS_path_df[AS_path_df.eq('29680 3257 7155')]))



as_path_list = AS_path_df.tolist()

total_as=[]

for i in range(len(as_path_list)):
    total_as.append(as_path_list[i].split(" "))

flat_list = [item for sublist in total_as for item in sublist]

#print(flat_list)
set_as_path = set(flat_list)
print(len(set_as_path))


#### PARTE 2

#AS_path_df = table_df['as_path']


total_len=0
for i in table_df['as_path']:
    total_len+=len(i.split(" "))
print(total_len/len(table_df))

total_as=0
for i in table_df['as_path']:
    total_as+=len(set(i.split(" ")))
print(total_as/len(table_df))


### PARTE 3

from collections import Counter

neighbors=[]
for i in table_df['as_path']:
    if len(i.split(" ")) == 1:
        continue
    else:
        neighbors.append(i.split(" ")[1])

print(len(set(neighbors)))

c = Counter(neighbors)

#print(most_common(c), c[most_common(c)])

print(c.most_common()[0])
