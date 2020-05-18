import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import sentiment as sa

tweets_list = [ line.rstrip('\n') for line in open(r"C:\Users\Monit\Downloads\Auspol_file.txt") ]
refined_tweets = sa.parse_tweets(tweets_list)
ptweets = [ tweet for tweet in refined_tweets if tweet[ 'sentiment' ] == 'positive' ]
ntweets = [ tweet for tweet in refined_tweets if tweet[ 'sentiment' ] == 'negative' ]

x = 100 * (len(ptweets) / len(refined_tweets))
y = 100 * (len(ntweets) / len(refined_tweets))
z = 100 * ((len(refined_tweets) - len(ntweets) - len(ptweets)) / len(refined_tweets))

sentiments = [ 'Positive', 'Negative', 'Neutral' ]

data = go.Pie(values=[ len(ptweets), len(ntweets), len(refined_tweets) ],
              showlegend=False)

data1 = go.Pie(labels=sentiments,
               values=[ x, y, z ],
               )

external_stylesheets = [ 'https://codepen.io/chriddyp/pen/bWLwgP.css 5' ]
colors = {
    'background': '#111111',
    'background2': '#FF0',
    'text': '#7FDBFF'
}

tab_1_layout = html.Div([
    html.Div([
        html.H3('Piechart1',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure={
                      'data': [ data ],
                      'layout': {
                          'plot_bgcolor': colors[ 'background' ],
                          'paper_bgcolor': colors[ 'background' ],
                          'font': {
                              'color': colors[ 'text' ],
                              'size': 18
                          },

                      }
                  },
                  style={'padding-right': '1px', 'z-index': '-2'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Piechart2', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure={
                      'data': [ data1 ],
                      'layout': {
                          'plot_bgcolor': colors[ 'background' ],
                          'paper_bgcolor': colors[ 'background' ],
                          'font': {
                              'color': colors[ 'text' ],
                              'size': 18
                          }
                      }
                  }
                  ),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
], style={'backgroundColor': 'yellow',})
