import pandas as pd
import numpy as np
df =pd.DataFrame(np.arange(12).reshape(3, 4), columns=['P', 'Q', 'R', 'S'])
df
df.drop(['Q','R'],axis=1)  #columns
df.drop(columns=['P', 'S'])
df.drop([0, 1])  #row
