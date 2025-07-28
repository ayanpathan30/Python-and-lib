# Measures of dispersion.
import pandas as pd
import numpy as np

df = pd.read_excel("merit_list.xlsx")

#print(df)

#Task1 Unique list of center names

centers = np.unique(df.center)

print("Centers: ",centers)

"""
#Task2 Centerwise no of candidates

centers,count = np.unique(df.center,return_counts=True)

print("\n\nCenterwise no of Candidates\n")
for i in range(0,len(count)):
    print(centers[i],"--",count[i])

print("-----------------------------")


#Task3 Markwise no of candidates

marks,count = np.unique(df.marks_interview,return_counts=True)

print("\n\nMarkwise Interview no of Candidates\n")
for i in range(0,len(count)):
    print(marks[i],"--",count[i])

print("-----------------------------")

#Task4 Genderwise no of candidates

gender,count = np.unique(df.gender,return_counts=True)

print("\n\nGenderwise  no of Candidates\n")
for i in range(0,len(count)):
    print(gender[i],"--",count[i])

print("-----------------------------") """

#Task5 frequency distribution considering following intervalsmfor total_marks:
# 81-84, 85-88.89-92,93-96,97-101

df = pd.read_excel("merit_list.xlsx",usecols=["total_marks"])

bins = [81,85,89,93,97,101]
labels = ["81 to 84","85 to 88","89 to 92","93 to 96","97 to 101"]

df["range"] = pd.cut(df.total_marks,bins,labels=labels)

print(df)

marks,count = np.unique(df.range,return_counts=True)

print("\n\nRangewise no of candidates\n")
for i in range(0,len(count)):
    print(marks[i],"--",count[i])

print("-----------------------------")
