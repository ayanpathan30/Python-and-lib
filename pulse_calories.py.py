import statistics as st
import pandas as pd
import numpy as np

pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

df = pd.read_excel("pulse_calories.xlsx")
#print(df)

#print("Before removing empty cell")
#print(df)
#df.dropna(inplace=True)
#print("After removing empty cell")
#print(df)

#df["Calories"].fillna(-99,inplace=True)
#print(df)

#mean_calories = np.mean(df.Calories)
#print("Mean calories= ",mean_calories)
#df["Calories"].fillna(mean_calories,inplace=True)
#print(df)

#df.loc[7,"Duration"] = np.mean(df.Duration) # df.loc[row_id,"column"] = new_value

df.drop_duplicates(inplace=True)
