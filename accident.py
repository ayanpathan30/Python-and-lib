# a5.2-2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("road_accidents.xlsx")
# print(df)
# #Task-2.1 
 
# x = df["year"].to_numpy() 
# y1 = df["accidents"].to_numpy() 
# plt.scatter(x, y1,marker="*")  
 
# y2 = df["casualty"].to_numpy() 
# plt.scatter(x, y2,marker="o") 
# plt.xlabel("Year") 
# plt.ylabel("No.of accidents/No. of casualties") 
# plt.title("Road Accidents Data") 
# plt.legend() 
# plt.show()

#Task-2.2 

x = df["year"].to_numpy() 
y1 = df["accidents"].to_numpy() 
plt.scatter(x, y1,c=y1,marker="X") 
plt.colorbar() 
y2 = df["casualty"].to_numpy() 
plt.scatter(x, y2,c=y2,marker="o") 
plt.colorbar() 
plt.xlabel("Year") 
plt.ylabel("No.of accidents/No. of casualties") 
plt.title("Road Accidents Data") 
plt.legend() 
plt.show() 