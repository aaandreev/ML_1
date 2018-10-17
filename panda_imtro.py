import pandas as pd

ds = pd.Series([1,2,3,4])
print(ds)

ds2 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
print(ds2)