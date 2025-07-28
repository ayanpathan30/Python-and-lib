import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("dataset_viz.xlsx")
#print(df)

x = df["Year"].to_numpy()  #Converting a dataframe column into an array
y1 = df["TVS"].to_numpy()  #Converting a dataframe column into an array

plt.plot(x,y1)

y2 = df["Honda"].to_numpy()
plt.plot(x,y2)

y3 = df["Hero"].to_numpy()
plt.plot(x,y3)

plt.xlabel("Year")
plt.ylabel("No. of two wheelers sold")
plt.title("Sales of two-wheelers")

plt.savefig("a5-1.png",transparent=True)
plt.savefig("a5-1.pdf")
plt.savefig("a5-1.jpg")
plt.savefig("a5-1.png")
plt.savefig("a5-1.png",facecolor="pink")

