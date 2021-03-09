import pandas as pd
import numpy as np
# creating a random dataFrame with 5 rows and 3 columns with random values
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)