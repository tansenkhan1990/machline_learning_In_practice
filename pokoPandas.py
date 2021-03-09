import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print('this is for one to 4 rows')
print (df.iloc[:4])
print('this is for slices 1-5 rows and 2-4 columns')
print( df.iloc[1:5, 2:4])