import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Загрузка данных из набора heart (statsmodels)
data = sm.datasets.heart.load_pandas().data

# Выбор столбцов и классов
age = data['age']  # возраст
survival = data['survival']  # выживаемость
classes = data['censors']  # классификация

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
for cls in classes.unique():
    plt.scatter(age[classes == cls], survival[classes == cls], label=f'Класс {cls}')

plt.xlabel('Возраст')
plt.ylabel('Выживаемость')
plt.title('Диаграмма рассеяния на основе данных heart')
plt.legend()
plt.show()

#######################################################################zadanie2(grafic2)
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Загрузка данных из набора longley
data = sm.datasets.longley.load_pandas().data

# Фильтрация данных по выборке (1951–1955 годы)
filtered_data = data[(data['YEAR'] >= 1951) & (data['YEAR'] <= 1955)]

# Выбор временных рядов
time_series = filtered_data[['GNPDEFL', 'UNEMP', 'ARMED']]

# Построение графиков
plt.figure(figsize=(12, 8))
for column in time_series.columns:
    plt.plot(filtered_data['YEAR'], time_series[column], label=column)

plt.xlabel('Год')
plt.ylabel('Значение')
plt.title('Динамика временных рядов (1951–1955 годы)')
plt.legend()
plt.grid()
plt.show()
