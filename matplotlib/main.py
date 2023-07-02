import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Создание данных
data = {
    'Марка': ['Audi', 'BMW', 'Mercedes', 'Toyota', 'Honda', 'Ford', 'Chevrolet', 'Volkswagen', 'Hyundai', 'Kia',
              'Mazda', 'Nissan', 'Subaru', 'Volvo', 'Lexus', 'Jeep', 'Tesla', 'Ferrari', 'Porsche', 'Lamborghini'],
    'Стоимость': [50000, 60000, 55000, 35000, 30000, 40000, 45000, 38000, 32000, 31000,
                  42000, 33000, 34000, 48000, 55000, 37000, 80000, 200000, 150000, 250000],
    'Потребление топлива': [10, 12, 11, 8, 9, 10, 11, 9, 8, 7,
                            9, 8, 8, 10, 11, 9, 5, 20, 18, 25],
    'Максимальная скорость': [220, 240, 230, 190, 200, 210, 200, 200, 190, 185,
                              210, 190, 195, 210, 230, 180, 250, 320, 300, 350],
    'Грузоподъемность': [500, 550, 520, 400, 450, 480, 470, 450, 400, 380,
                         420, 390, 400, 480, 500, 370, 300, 200, 250, 180]
}

# Создание DataFrame из данных
df = pd.DataFrame(data)

# Создание xls-документа
df.to_excel('автомобили.xlsx', index=False)

# Визуализация зависимости: потребление топлива от стоимости (линейная диаграмма)
plt.figure(figsize=(8, 6))
sns.set(font_scale=0.5)
plt.plot(sorted(df['Стоимость']), sorted(df['Потребление топлива']), 'bo-')
plt.ylabel('Стоимость')
plt.xlabel('Потребление топлива')
plt.title('Зависимость потребления топлива от стоимости автомобиля')
plt.grid(True)
plt.show()

# Визуализация зависимости: потребление топлива от скорости (точечный график)
plt.figure(figsize=(8, 6))
plt.scatter(sorted(df['Максимальная скорость']), sorted(df['Потребление топлива']), c='r', marker='o')
plt.xlabel('Максимальная скорость')
plt.ylabel('Потребление топлива')
plt.title('Зависимость потребления топлива от скорости автомобиля')
plt.grid(True)
plt.show()

# Визуализация зависимости: грузоподъемностиот скорости (точечный график)
plt.figure(figsize=(8, 6))
plt.scatter(sorted(df['Максимальная скорость']), sorted(df['Грузоподъемность']), c='g', marker='o')
plt.xlabel('Максимальная скорость')
plt.ylabel('Грузоподъемность')
plt.title('Зависимость грузоподъемности от скорости автомобиля')
plt.grid(True)
plt.show()

# Построение гистограммы для разделения автомобилей на 5 групп по скорости
plt.figure(figsize=(8, 6))
plt.hist(sorted(df['Максимальная скорость']), bins=5, edgecolor='black')
plt.xlabel('Максимальная скорость')
plt.ylabel('Количество автомобилей')
plt.title('Распределение автомобилей по скорости')
plt.grid(True)
plt.show()

# Построение коробочного графика для отображения скоростей разных марок
plt.figure(figsize=(8, 6))
plt.boxplot([df[df['Марка'] == brand]['Максимальная скорость'] for brand in df['Марка']])
plt.xticks(range(1, len(df['Марка'].unique()) + 1), df['Марка'].unique(), rotation=90)
plt.xlabel('Марка автомобиля')
plt.ylabel('Максимальная скорость')
plt.title('Сравнение скоростей разных марок автомобилей')
plt.grid(True)
plt.show()

# Построение парного графика для отображения зависимости величин датасета
sns.set_style("white")
plt.figure(figsize=(10, 8))
sns.pairplot(df)
plt.show()

