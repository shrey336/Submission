import pandas as pd


#Reading the input file as pandas data frames
df=pd.read_csv("filteredCountry.csv")
print(df)

df=df[['SKU', 'PRICE']]
print(df)
df.groupby('SKU')['PRICE'].count().sort_values(ascending=True)
print(df)
df=df[['SKU', 'PRICE']]
print(df)
df.to_csv("demo1.csv")
#indices = df.groupby('SKU')['PRICE'].idxmin
#df.loc[indices]

"""df=df.sort_values(by=['PRICE'])
df=list(df)
df=df['SKU', 'PRICE']
print(df)"""




