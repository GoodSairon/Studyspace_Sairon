from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
df=pd.DataFrame({'id':np.linspace(0,10,10),
            'Y1':np.random.randn(10),'Y11':np.random.randn(10), # 2 графика первого subplot
             'Y2':np.random.randn(10),'Y22':np.random.randn(10), # 2 графика второго subplot
            'Y3':np.random.randn(10),'Y33':np.random.randn(10)  # 2 графика третьего subplot
             })

trace1=go.Scatter(x=df['id'],y=df['Y1'])
trace2=go.Scatter(x=df['id'],y=df['Y11'])
data1=[trace1,trace2]

trace3=go.Scatter(x=df['id'],y=df['Y2'])
trace4=go.Scatter(x=df['id'],y=df['Y22'])
data2=[trace3,trace4]

trace5=go.Scatter(x=df['id'],y=df['Y3'])
trace6=go.Scatter(x=df['id'],y=df['Y33'])
data3=[trace5,trace6]

fig = make_subplots(rows=3, cols=1)

for x in data1:
    fig.add_trace(x,row=1, col=1)

for x in data2:
    fig.add_trace(x,row=2, col=1)

for x in data3:
    fig.add_trace(x,row=3, col=1)


fig.update_layout(height=600, width=600, title_text="Subplots")
fig.show()
