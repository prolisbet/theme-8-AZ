import pandas as pd

df = pd.read_csv("dz.csv")

print(df.head())

print(df.info())

print(df.describe())

print(df['City'].tolist())
print(df['Salary'].tolist())

df['City'].fillna(value='Не указан', inplace=True)
df['Salary'].fillna(value=0, inplace=True)
print(df)

series = df.groupby('City')['Salary'].mean()
series_df = series.reset_index()

series_df.columns = ['City', 'Mean salary']
series_df = series_df.sort_values('Mean salary', ascending=False)

print(series_df)
