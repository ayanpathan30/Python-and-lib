#a5-4
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("dataset_viz.xlsx","Sheet4")
#print(df)

x = df["Year"].to_numpy()
y1 = df["Maruti Suzuki"].to_numpy()
y2 = df["Hyundai"].to_numpy()


plt.scatter(x,y1,c=y1)
plt.scatter(x,y2,c=y2)

plt.colorbar()