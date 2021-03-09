import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print( df.iloc[3])
print(df.loc['d'])
print('this is the dataFrame')
print(df)
print('this is index')
print(df.columns)
print('this is rows')
print(df.values)