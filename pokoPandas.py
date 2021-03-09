import pandas as pd
import numpy as np

data = np.array([['Alex',10],['Bob',12],['Clarke',13]])
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)