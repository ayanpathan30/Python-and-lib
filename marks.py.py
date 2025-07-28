import statistics as st
import pandas as pd
import numpy as np

df = pd.read_excel("marks_abc.xlsx")
#print(df)

#print(np.mean(df)) #Mean of all the values from all rows and columns

#print(df.mean())    # Mean of all columns

avg_a = np.mean(df.marks_a)
print("Average marks in subject a = ",avg_a)

df["total_marks"] = df.marks_a + df.marks_b + df.marks_c

print(df)

avg_total_marks = np.mean(df.total_marks)
print("Average total marks = ",avg_total_marks)

median_a = np.median(df.marks_a)
print("Median marks in subject a = ",median_a)

mode_c = st.mode(df.marks_c)
print("Marks which occur most of times in subject c = ",mode_c)

q1 = np.percentile(df.marks_a,25)
q3 = np.percentile(df.marks_a,75)
qd = (q3-q1)/2
print("q1 = ",q1)
print("q3 = ",q3)
print("Quaartile deviation of a = ",qd)


print(np.var(df.marks_a))
print(np.var(df.marks_b))
print(np.var(df.marks_c))

#Standard deviation
sd_a=(np.std(df.marks_a))
print("Standard deviation of mark_a = ",sd_a)
sd_b=(np.std(df.marks_b))
print("Standard deviation of mark_b = ",sd_b)
sd_a=(np.std(df.marks_c))
print("Standard deviation of mark_a = ",sd_c)








