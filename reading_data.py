import pandas as pd
import numpy as np

#ipython.sendFileContentsToIPython

#read an excel spreadsheet

tracks = pd.read_excel('.\\pandas\\Tracks.xlsx', sheet_name=0)
# print(tracks)
# print(tracks.columns)
# print(tracks['Milliseconds'])

flights = pd.read_csv('.\\pandas\\flights.csv', index_col=False)
print(flights)
