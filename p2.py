import pandas as pd
import math
table_df=pd.read_csv('https://www.it.uc3m.es/alberto/AI/2021-03-02.topSites_ES.traceroute_info_monitor01', delimiter=',')


print('COMPLETE', len(table_df[table_df['status']=='COMPLETE']))
print('DESTINATION_NOT_RESOLVED', len(table_df[table_df['status']=='DESTINATION_NOT_RESOLVED']))
print('INCOMPLETE', len(table_df[table_df['status']=='INCOMPLETE']))

###

hops = 0.0
for i in table_df['hop_count']:
    if math.isnan(i):
        continue
    else:
        hops=hops+i
print(hops)
print(hops/len(table_df))

###

hops = 0.0
completed = table_df[table_df['status']=='COMPLETE']
for i in completed['hop_count']:
    if math.isnan(i):
        continue
    else:
        hops=hops+i
print(hops)
print(hops/len(table_df))

###
table_ms =table_df.copy()
table_ms.drop(columns=['status','traces','hop_count','last_hop_resolved'],inplace=True)
print('\n10 mas cercanos\n',table_ms.sort_values(by=['ms'],ascending=True).head(10))
print('\n10 mas lejanos\n',table_ms.sort_values(by=['ms'],ascending=False).head(10))


### Parte 2

table_df.dropna(subset=['last_hop_resolved'], inplace=True)

names=[]
for i in table_df['last_hop_resolved']:
    last_two = '.'.join(i.split('.')[-2:])
    names.append(last_two)
table_df['last_two'] = names

by_last_two=table_df.groupby(by='last_two')

print(by_last_two.size().sort_values(ascending=False).head(5))

###
table_df.drop(columns=['status','traces','hop_count'],inplace=True)
print(table_df[table_df['last_two']=='amazonaws.com'].sort_values(by=['ms'],ascending=True).head(5))
