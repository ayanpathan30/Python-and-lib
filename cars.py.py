#Row operations on a database.

import pandas as pd
df = pd.read_csv("cars.csv")

print("Dataframe before deleting rows...")
#print(df)

#print(df.loc[10])

#print(df.loc[0:5])

#print(df.loc[:-3])

#print(df.loc[[0,2,3,6]])

#print(df.loc[df.CO2<=100])

#print(df.loc[df.Car=='Ford'])

#print(df.loc[(df.Weight>=1000)&(df.Weight<=1500)])

#print(df.loc[(df.Car=="Audi")|(df.CO2>110)])

#print(df[df.Car=="Volvo"].index)

df.drop(df[df.Car=="Volvo"].index,axis=0,inplace=True)
print("Dataframe after deleting rows...")
print(df)

df.drop(df[(df.Car=="BMW")|(df.CO2>115)].index,axis=0,inplace=True)
print(df)
