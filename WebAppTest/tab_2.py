#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------
import requests
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import DataExtractor as de


cities = ["Adelaide","Brisbane","Melbourne","Perth","Sydney"]
colors1 = ["red","orange","blue","green","yellow"]
unique_user = de.unique_user_cities()
voters = de.voters_data()

twitter = go.Pie(labels = cities,values=unique_user)
aurin = go.Pie(labels = cities, values = voters)


tab_2_layout = html.Div([
    html.Div([
        html.H3('Distribution of twitter users across cities',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure={
                      'data': [ twitter ],
                  },
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Eligible voters across cities', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure={
                      'data': [ aurin ]
                  }
                  ),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])
