from plotly.subplots import make_subplots
import pandas as pd
import plotly as pl
import plotly.express as px
import plotly.graph_objs as pgo
import seaborn as sns
import matplotlib.pyplot as plt
import sweetviz as sw

data = {
    'Місто': ['Київ', 'Харків', 'Одеса', 'Дніпро', 'Донецьк', 'Запоріжжя', 'Львів', 'Кривий Ріг', 'Миколаїв', 'Маріуполь', 'Вінниця', 'Херсон', 'Полтава', 'Чернігів', 'Черкаси', 'Житомир', 'Івано-Франківськ', 'Кам\'янське', 'Кропивницький', 'Луцьк'],
    'Населення': [3000000, 1500000, 1000000, 1000000, 950000, 900000, 800000, 700000, 550000, 500000, 400000, 350000, 300000, 300000, 280000, 250000, 230000, 220000, 210000, 200000],
    'Середній дохід': [80000, 60000, 55000, 60000, 50000, 48000, 55000, 45000, 42000, 40000, 45000, 42000, 40000, 40000, 38000, 36000, 42000, 36000, 35000, 38000],
    'Площа': [847, 350, 162, 405, 358, 334, 182, 430, 260, 205, 240, 260, 103, 79, 69, 72, 84, 93, 103, 42],
    'Метро': ['Так', 'Так', 'Так', 'Так', 'Ні', 'Ні', 'Так', 'Ні', 'Так', 'Ні', 'Ні', 'Так', 'Ні', 'Ні', 'Ні', 'Ні', 'Ні', 'Ні', 'Ні', 'Ні']
}

df = pd.DataFrame(data)

fig1 = pgo.Scatter(x=sorted(df['Населення']), y=sorted(df['Площа']))
fig2 = pgo.Scatter(x=sorted(df['Середній дохід']), y=sorted(df['Населення']))
fig = make_subplots(rows=1, cols=2)

fig.add_trace(fig1, row=1, col=1)
fig.add_trace(fig2, row=1, col=2)
fig.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df[['Населення', 'Середній дохід', 'Площа']].corr(), annot=True)
plt.show()

df.to_excel('df.xlsx', index=False)
df = pd.read_excel('df.xlsx')

report = sw.analyze(df)
report.show_html()

