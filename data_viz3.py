# a5-3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("dataset_viz.xlsx","Sheet3")
#print(df)
values =df["Intake"].to_numpy()
#labels =df["Programme"].to_numpy()
labels=df["Programme"]+" ["+df["Intake"].astype(str)+"]"

#plt.pie(values,labels=labels,autopct="%1.1f%%")
plt.pie(values,labels=labels,autopct="%1.1f%%",counterclock=False)

