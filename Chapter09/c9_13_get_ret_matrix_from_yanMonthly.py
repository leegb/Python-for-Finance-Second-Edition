"""
  Name     : c9_13_get_ret_matrix_from_yanMonthly.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
import pandas as pd
import numpy as np

n_stocks=10
x=pd.read_pickle('c:/temp/yanMonthly.pkl')
x2=sp.unique(np.array(x.index))
x3=x2[x2<'ZZZZ']                       # remove all indices
sp.random.seed(1234567)

nonStocks=['GOLDPRICE','HML','SMB','Mkt_Rf','Rf','Russ3000E_D','US_DEBT',
   'Russ3000E_X','US_GDP2009dollar','US_GDP2013dollar']

x4=list(x3)
for i in range(len(nonStocks)):
    x4.remove(nonStocks[i])

k=sp.random.uniform(low=1,high=len(x4),size=n_stocks)
y,s=[],[]

for i in range(n_stocks):
    index=int(k[i])
    y.append(index)
    s.append(x4[index])
final=sp.unique(y)
#print(final)
print(s)


#final=pd.merge(x2,ff,left_index=True,right_index=True)
#print(final.head())
