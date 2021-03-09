
import pandas as pd
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
print('this is the dataFrame')
print(df)
print('this is drop columns')
x,y = df
print(x)
print(y)

df = df.drop(0)
print('this is the DataFrame after the drop')
print(df)