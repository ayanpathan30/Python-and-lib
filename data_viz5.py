#a5-5
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("dataset_viz.xlsx","Sheet5")
#print(df)

x = df["Business"].to_numpy()
y = df["Revenue"].to_numpy()

for i in range(len(y)):
    plt.text(i,y[i],y[i],ha="center")
    
#plt.bar(x,y,width=0.3,color="red")


plt.barh(x,y,color="red",height=0.3)


#no-2

x = df["Business"].to_numpy()
y = df["Percentage"].to_numpy()


plt.xlabel("Range of Business")
plt.ylabel("No. of Percentage")
plt.title("Percentage analysis")

color = ["red","green","blue","yellow"]
plt.barh(x,y,color=color,height=0.3)