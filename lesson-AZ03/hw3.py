import pandas as pd
import matplotlib.pyplot as plt

# Использую спарсенный в предыдущем модуле полный каталог продукции divan.ru
df = pd.read_csv('divan_ru_catalogue.csv')

df_filtered = df[(df['Категория товара'] == 'Диваны и кресла') & (df['Название товара'].str.contains(
    'Диван', case=False))]

df_filtered['Цена товара'] = df_filtered['Цена товара'].replace('[^\d.]', '', regex=True).replace(
    ' ', '').astype(float).astype(int)

df_filtered = df_filtered.drop(columns=['Ссылка на товар'])

print(df_filtered.head(10))
print(df_filtered.info())
print(df_filtered.describe())

mean_price = df_filtered["Цена товара"].mean()
median_price = df_filtered["Цена товара"].median()
Q1_price = df_filtered["Цена товара"].quantile(0.25)
Q3_price = df_filtered["Цена товара"].quantile(0.75)
IQR = Q3_price - Q1_price
downside = Q1_price - 1.5 * IQR
upside = Q3_price + 1.5 * IQR

print(f'\nСредняя цена дивана - {mean_price:.2f}')
print(f'Медианная цена дивана - {median_price:.2f}')
print(f'Первый квартиль цен - {Q1_price:.2f}')
print(f'Третий квартиль цен - {Q3_price:.2f}')
print(f'Межквартальный размах (IQR) для цен - {IQR}')
print(f'Нижняя граница цен - {downside}')
print(f'Верхняя граница цен - {upside}')

plt.hist(df_filtered['Цена товара'], bins=20, color='lightblue', edgecolor='black', linewidth=0.2)

plt.title('Гистограмма цен на диваны на сайте divan.ru')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.axvline(mean_price, color='green', label='Средняя цена')
plt.axvline(median_price, color='red', label='Медианная цена')
plt.axvline(Q1_price, color='orange', label='Первый квартиль')
plt.axvline(Q3_price, color='pink', label='Третий квартиль')
plt.legend()
plt.grid(axis='y', linewidth=0.5, linestyle='--')

plt.show()
