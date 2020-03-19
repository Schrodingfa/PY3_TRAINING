# Author:jxy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_excel(r"C:\Users\admin\Desktop\test.xlsx", sheet_name="目录")
# df = pd.read_csv(r"C:\Users\admin\Desktop\test1.csv", sep="@#", engine='python', encoding='utf-8')
df = pd.read_csv(r"C:\Users\admin\Desktop\test2.csv", sep="|", header=None)

print(df)

df.columns = ["id", "county", "room", "address1", "address2", "date", "value"]

# print(df[df["value"] > -27][["county", "address1", "value"]])
print(df.sort_values(by=["value"], ascending=False))
# df.index = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# print(df.iloc[3:8, [2, 4, 6]])
# print(df['ID'].dtype)
# print(df['ID'].astype("float64"))
# print(df.describe())
# print(df.info())
# df1 = df.fillna(0)
# print(df1)
# print(df.shape)
