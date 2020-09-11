import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("IMVA.xlsx")
print("********Countries********")
df1 = df[["Periods", " United Kingdom ", " Germany ", " France ", " Italy ", " Netherlands ", " Greece ", " Belgium & Luxembourg "," Switzerland ",	" Austria ", " Scandinavia "]]
#print(df)
#print(df1)
print("********Split********")
Countries = df1['Periods'].str.split(' ', n = 2, expand = True)
#print(Countries)
print("********Assign a new column named year and month********")
df1 = df1.assign(year=Countries[1])
df1 = df1.assign(month=Countries[2])
#print(df1.dtypes)
#print(df1)
print("********Convert********")
df1["year"] = pd.to_numeric(df1["year"])
#print(df1.dtypes)
print("********TOP 3 Countries********")
df3 = df1[(df1["year"] >= 2008) & (df1["year"] <= 2017)]
df4 = df3[[" Germany ", " France ", " Italy ", " Netherlands ", " Greece ", " Belgium & Luxembourg "," Switzerland ",	" Austria ", " Scandinavia "]]
ps = df4.sum().sort_values(ascending=False)
top3countries = ps.head(3)
top3countries.index
#print(ps)
#print(top3countries)
index = np.arange(len(top3countries.index))
plt.figure(figsize=(10, 10))
plt.xlabel('Countries (Others)', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, top3countries.index, fontsize=7, rotation=60)
plt.title('Top 3 Europe Countries from 2008-2017 (Period 2008-2017)')
plt.bar(top3countries.index, top3countries.values/1000)
plt.show();
print("********ALL Europe Countries********")
index = np.arange(len(ps.index))
plt.xlabel('Countries (Others)', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=7, rotation=60)
plt.title('Total Europe Countries from 2008-2017 (Period 2008-2017)')
plt.bar(ps.index, ps.values/1000)
plt.show();