import numpy as np
import pandas as pd

labels =['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30 }

print(pd.Series(data=my_data))


print(pd.Series(data=my_data,index=labels))

print(pd.Series(my_data,labels))
as

ax
1
2