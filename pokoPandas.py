import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
print('this is dataFrame')
print(df)
for row_index,row in df.iterrows():
   print('this is row index')
   print(row_index)
   print('row')
   print(row)
   print('last item')
   print(row_index,row)