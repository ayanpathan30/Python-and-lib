#a5-2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("dataset_viz.xlsx","Sheet2")
#print(df)

values = df["marks"].to_numpy()
bins=10
range = (0,100)

plt.hist(values,bins=bins,range=range,rwidth=0.3,color="red")

plt.xlabel("Range of marks")
plt.ylabel("No. of students")
plt.title("Result analysis")
