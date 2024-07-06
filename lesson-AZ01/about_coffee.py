import pandas as pd

df = pd.read_csv("Coffee_domestic_consumption.csv")

print(df.head())

print(df.info())

print(df.describe())

df_mini = df[["Country", "Coffee type", "Total_domestic_consumption"]]

df_mini = df_mini.sort_values("Total_domestic_consumption", ascending=False)

df_mini = df_mini.rename(columns={"Total_domestic_consumption": "TDC"})

print(df_mini.head())

print(df_mini.info())

series_grouped = df_mini.groupby('Coffee type')["TDC"].mean()

print(series_grouped)

df_grouped = series_grouped.reset_index()

df_grouped.columns = ['Coffee type', 'Mean TDC']

max_tdc = df_mini.groupby('Coffee type')['TDC'].max()
min_tdc = df_mini.groupby('Coffee type')['TDC'].min()

df_grouped['Max TDC'] = max_tdc.values
df_grouped['Min TDC'] = min_tdc.values

print(df_grouped)

max_tdc_country = df_mini.loc[df_mini.groupby('Coffee type')['TDC'].idxmax()]['Country']
min_tdc_country = df_mini.loc[df_mini.groupby('Coffee type')['TDC'].idxmin()]['Country']

df_grouped['Country max'] = max_tdc_country.values
df_grouped['Country min'] = min_tdc_country.values

print(df_grouped)

# print(f"Наибольшее потребление")
