# Basic dataset operations

import pandas as pd
print("pandas imported successfully")

df = pd.read_csv("diabetes.csv");
print("Dataset loaded successfully..")

r = df.shape[0]
c = df.shape[1]

print("No of rows = ",r)
print("No of columns = ",c)

print("Basic stats of dataset is as follows:")
print(df.describe())

print("Basic info of dataset columns:")
print(df.info())

# to display first five records
print(df.head())

# to display first ten records
print(df.head(10))

# To display last five records
print(df.tail())

# To display last ten records
print(df.tail(10))

# To display single column
print(df["Age"])

# To display multiple column
print(df[["Age","BMI","Outcome"]])

df.loc[df.Age==50]

df.drop("SkinThickness",axis=1,inplace=True)

