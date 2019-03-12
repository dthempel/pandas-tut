import pandas as pd
import numpy as np

#ipython.sendFileContentsToIPython

#DataFrame: a 2D table with rows and columns

df_data = {
    'col1': np.random.rand(5),
    'col2': np.random.rand(5),
    'col3': np.random.rand(5)
}

df = pd.DataFrame(df_data)
print(df)

# fetch rows

print(df[:2])

# fetch columns

print(df['col1'])

# fetch multiple columns

print(df[['col1', 'col2']])