import numpy as np

prices = np.array([60000, 800, 1000])
print(prices)
print('Average:', np.mean(prices))
print('Maximum:', np.max(prices))
print('Minimum:', np.min(prices))


import pandas as pd

df = pd.read_csv("ev_sessions.csv")

print(df)
print(df.columns)
print(df.shape)
print(df.dtypes)

print(df[["Station", "kWh", "Amount"]])