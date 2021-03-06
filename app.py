
# coding: utf-8

# In[ ]:

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

df = pd.read_csv('http://7xpvdr.com1.z0.glb.clouddn.com/nama_10_gdp_1_Data_2.csv')

available_indicatorsX = df['NA_ITEM'].unique()
available_indicatorsY = df['NA_ITEM'].unique()

available_indicatorsX_lineChart = df['GEO'].unique()
available_indicatorsY_lineChart = df['NA_ITEM'].unique()

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicatorsX],
                value='Gross domestic product at market prices'
            )
            # dcc.RadioItems(
                # id='xaxis-type',
                # options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                # value='Linear',
                # labelStyle={'display': 'inline-block'}
            # )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicatorsY],
                value='Value added, gross'
            )
		# dcc.RadioItems(
                # id='yaxis-type',
                # options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                # value='Linear',
                # labelStyle={'display': 'inline-block'}
            # )

        ],
        style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        id='year--slider',
        min=df['TIME'].min(),
        max=df['TIME'].max(),
        value=df['TIME'].max(),
        step=None,
        marks={str(year): str(year) for year in df['TIME'].unique()}
    ),

#####################

    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column_LC',
                options=[{'label': i, 'value': i} for i in available_indicatorsX_lineChart],
                value='European Union (28 countries)'
            )
            # dcc.RadioItems(
                # id='xaxis-type_LC',
                # options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                # value='Linear',
                # labelStyle={'display': 'inline-block'}
            # )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column_LC',
                options=[{'label': i, 'value': i} for i in available_indicatorsY_lineChart],
                value='Gross domestic product at market prices'
            )
            # dcc.RadioItems(
                # id='yaxis-type_LC',
                # options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                # value='Linear',
                # labelStyle={'display': 'inline-block'}
            # )

        ],
        style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='line-chart')
])

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
     dash.dependencies.Input('yaxis-column', 'value'),
     dash.dependencies.Input('year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name, year_value):
    dff = df[df['TIME'] == year_value]
    return {
        'data': [go.Scatter(
            x=dff[dff['NA_ITEM'] == xaxis_column_name]['Value'],
            y=dff[dff['NA_ITEM'] == yaxis_column_name]['Value'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name
                # 'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name
                # 'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

@app.callback(
    dash.dependencies.Output('line-chart', 'figure'),
    [dash.dependencies.Input('xaxis-column_LC', 'value'),
     dash.dependencies.Input('yaxis-column_LC', 'value')])
def update_graph_lineChart(xaxis_column_name, yaxis_column_name):
    #dff = df[df['TIME'] == year_value]
    
    return {
        'data': [go.Scatter(
            x = df['TIME'].unique(), 
            y = df[(df['NA_ITEM'] == yaxis_column_name) & (df['GEO'] == xaxis_column_name)]['Value'],
            #x=dff[dff['GEO'] == xaxis_column_name]['Value'],
            #y=dff[dff['NA_ITEM'] == yaxis_column_name]['Value'],
            mode='line',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': 'year'
            },
            yaxis={
                'title': yaxis_column_name
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()


# In[ ]:




# In[ ]:



