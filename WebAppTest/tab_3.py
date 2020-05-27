#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import DataExtractor as de

cities = ["Adelaide","Brisbane","Melbourne","Perth","Sydney"]

age = ["Youth","Adult","Senior-citizens"]
melbourne_count = de.age_data("Melbourne")
sydney_count = de.age_data("Sydney")
perth_count = de.age_data("Perth")
adelaide_count = de.age_data("Adelaide")
brisbane_count = de.age_data("Brisbane")

unique_user=de.unique_user_cities()

twitter = go.Pie(labels = cities,values=unique_user)
youth_data = [adelaide_count[0],brisbane_count[0],melbourne_count[0],perth_count[0],sydney_count[0]]
aurin_data = go.Bar(x=cities,y=youth_data)


tab_3_layout = html.Div([
    html.Div([
        html.H3('Distribution of twitter users across cities',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure={
                      'data': [ twitter ]
                  },
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Age Demography across cities', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure={
                      'data': [ aurin_data ]
                  }
                  ),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])
