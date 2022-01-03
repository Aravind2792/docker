import plotly 
import dash 
from dash import html
from dash import dcc
from plotly import graph_objs as go
import numpy as np
import pandas as pd

df=pd.read_excel('Alathiyur CM1 data.xlsx')
app=dash.Dash()
app.layout=html.Div([
    dcc.Graph(id="Test_plot",
             figure={
                 'data':[go.Scatter(x=df['Feed'],y=df['DP'],mode='lines')],
                 'layout':go.Layout(title="Test plot",xaxis={'title':"Feed"},yaxis={'title':'DP'},hovermode='closest')
                    }
             )
           ])
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8080, debug=True)           
