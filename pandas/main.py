import pandas as pd
import random as rand

def next(mark_list):

    for mark in mark_list:
        if mark >= 3:
            True
        else:
            False

df = pd.DataFrame({
                    'name': ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6', 'Name7', 'Name8', 'Name9', 'Name10', 'Name11', 'Name12', 'Name13', 'Name14', 'Name15'],
                    'surname': ['Surname1', 'Surname2', 'Surname3', 'Surname4', 'Surname5', 'Surname6', 'Surname7', 'Surname8', 'Surname9', 'Surname10', 'Surname11', 'Surname12', 'Surname13', 'Surname14', 'Surname15'],
                    'average': [rand.uniform(2.5, 5.0) for _ in range(0, 15)],
                    'mark': [rand.randint(2,5) for _ in range(0, 15)],
                    'attempts': [rand.randint(1, 3) for _ in range(0, 15)]
                    })

df['access'] = False
df.loc[df['average'] >= 3.0, 'access'] = True

print(df)
print('min: ', df.average.min())
print('max: ', df.average.max())
print('average :', df.average.mean())
print('median: ', df.average.median())

nm_qu = 0

for attempts in df.attempts.items():

    att_lst = list(attempts)

    if att_lst[1] == 1:
        nm_qu += 1

print('first attempt:', nm_qu)

series = pd.Series([list(names)[1] for names in df.name.items()])

print(series)


