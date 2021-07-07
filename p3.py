import pandas as pd
import math
table_df=pd.read_csv('https://www.it.uc3m.es/alberto/AI/2021-03-02.HOPS', delimiter=',')

fifth_hop=[]
for i in table_df['5']:
    fifth_hop.append(i)
if '*' in fifth_hop:
    fifth_hop.remove('*')

sixth_hop =[]
for i in table_df['6']:
    sixth_hop.append(i)
if '*' in sixth_hop:
    sixth_hop.remove('*')

print('Numero de saltos distintos en la posicion 5: ',len(set(fifth_hop)))

print('Numero de saltos distintos en la posicion 6: ',len(set(sixth_hop)))
