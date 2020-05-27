#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------
import plotly.graph_objs as go
from app import *
import DataExtractor as de

year = [2017,2018,2019,2020]

#Brisbane
layout = go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                   plot_bgcolor='rgba(0,0,0,0)',xaxis={'tickformat':'d'})

twitter_positive_coalition_b =  go.Scatter(x=year,y=de.positive_coalition("Brisbane"), name = "Coalition")
twitter_positive_labor_b =  go.Scatter(x=year,y=de.positive_labor("Brisbane"), name="Labor")
positive_b = [twitter_positive_coalition_b , twitter_positive_labor_b ]
fig_positive_b = go.Figure(data=positive_b, layout=layout)
fig_positive_b.update_layout(xaxis_title="Year",yaxis_title="Percentage")


twitter_negative_coalition_b = go.Scatter(x=year,y=de.negative_coalition("Brisbane"), name = "Coalition")
twitter_negative_labor_b = go.Scatter(x=year,y=de.negative_labor("Brisbane"), name = "Labor")
negative_b = [twitter_negative_coalition_b,twitter_negative_labor_b]
fig_negative_b = go.Figure(data=negative_b, layout=layout)
fig_negative_b.update_layout(xaxis_title="Year",yaxis_title="Percentage")


aurin_data_2016_b = go.Bar(x=[2016,2019],y=de.aurinPartyData2016("Brisbane"),name="Coalition")
aurin_data_2019_b = go.Bar(x=[2016,2019],y=de.aurinPartyData2019("Brisbane"),name = "Labor")

fig_aurin_b = go.Figure(data=[aurin_data_2016_b,aurin_data_2019_b])
fig_aurin_b.update_layout(barmode='group',xaxis_title= "Year",yaxis_title="Voters Count")


tab_1_layout_brisbane_positive = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_positive_b,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_b),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

tab_1_layout_brisbane_negative = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_negative_b,
                  style={'padding-right': '1px', 'z-index': '-2'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_b),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

#Adelaide

twitter_positive_coalition_a =  go.Scatter(x=year,y=de.positive_coalition("Adelaide"), name = "Coalition")
twitter_positive_labor_a =  go.Scatter(x=year,y=de.positive_labor("Adelaide"), name="Labor")
positive_a = [twitter_positive_coalition_a , twitter_positive_labor_a ]
fig_positive_a = go.Figure(data=positive_a, layout=layout)
fig_positive_a.update_layout(xaxis_title="Year",yaxis_title="Percentage")


twitter_negative_coalition_a = go.Scatter(x=year,y=de.negative_coalition("Adelaide"), name = "Coalition")
twitter_negative_labor_a = go.Scatter(x=year,y=de.negative_labor("Adelaide"), name = "Labor")
negative_a = [twitter_negative_coalition_a,twitter_negative_labor_a]
fig_negative_a = go.Figure(data=negative_a, layout=layout)
fig_negative_a.update_layout(xaxis_title="Year",yaxis_title="Percentage")

aurin_data_2016_a = go.Bar(x=[2016,2019],y=de.aurinPartyData2016("Adelaide"),name="Coalition")
aurin_data_2019_a = go.Bar(x=[2016,2019],y=de.aurinPartyData2019("Adelaide"),name = "Labor")
fig_aurin_a = go.Figure(data=[aurin_data_2016_a,aurin_data_2019_a])
fig_aurin_a.update_layout(barmode='group',xaxis_title="Year",yaxis_title="Voters Count")


tab_1_layout_adelaide_positive = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_positive_a,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_a),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

tab_1_layout_adelaide_negative = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_negative_a,
                  style={'padding-right': '1px', 'z-index': '-2'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_a),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

#Melbourne

twitter_positive_coalition_m =  go.Scatter(x=year,y=de.positive_coalition("Melbourne"), name = "Coalition")
twitter_positive_labor_m =  go.Scatter(x=year,y=de.positive_labor("Melbourne"), name="Labor")
positive_m = [twitter_positive_coalition_m , twitter_positive_labor_m ]
fig_positive_m = go.Figure(data=positive_m, layout=layout)
fig_positive_m.update_layout(xaxis_title="Year",yaxis_title="Percentage")


twitter_negative_coalition_m = go.Scatter(x=year,y=de.negative_coalition("Melbourne"), name = "Coalition")
twitter_negative_labor_m = go.Scatter(x=year,y=de.negative_labor("Melbourne"), name = "Labor")
negative_m = [twitter_negative_coalition_m,twitter_negative_labor_m]
fig_negative_m = go.Figure(data=negative_m, layout=layout)
fig_negative_m.update_layout(xaxis_title="Year",yaxis_title="Percentage")

aurin_data_2016_m = go.Bar(x=[2016,2019],y=de.aurinPartyData2016("Melbourne"),name="Coalition")
aurin_data_2019_m = go.Bar(x=[2016,2019],y=de.aurinPartyData2019("Melbourne"),name = "Labor")
fig_aurin_m = go.Figure(data=[aurin_data_2016_m,aurin_data_2019_m])
fig_aurin_m.update_layout(barmode='group',xaxis_title="Year",yaxis_title="Voters Count")


tab_1_layout_melbourne_positive = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_positive_m,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_m),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

tab_1_layout_melbourne_negative = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_negative_m,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_m),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

#Perth
twitter_positive_coalition_p =  go.Scatter(x=year,y=de.positive_coalition("Perth"), name = "Coalition")
twitter_positive_labor_p =  go.Scatter(x=year,y=de.positive_labor("Perth"), name="Labor")
positive_p = [twitter_positive_coalition_p , twitter_positive_labor_p ]
fig_positive_p = go.Figure(data=positive_p, layout=layout)
fig_positive_p.update_layout(xaxis_title="Year",yaxis_title="Percentage")


twitter_negative_coalition_p = go.Scatter(x=year,y=de.negative_coalition("Perth"), name = "Coalition")
twitter_negative_labor_p = go.Scatter(x=year,y=de.negative_labor("Perth"), name = "Labor")
negative_p = [twitter_negative_coalition_p,twitter_negative_labor_p]
fig_negative_p = go.Figure(data=negative_p, layout=layout)
fig_negative_p.update_layout(xaxis_title="Year",yaxis_title="Percentage")



aurin_data_2016_p = go.Bar(x=[2016,2019],y=de.aurinPartyData2016("Perth"),name="Coalition")
aurin_data_2019_p = go.Bar(x=[2016,2019],y=de.aurinPartyData2019("Perth"),name = "Labor")
fig_aurin_p = go.Figure(data=[aurin_data_2016_p,aurin_data_2019_p])
fig_aurin_p.update_layout(barmode='group',xaxis_title="Year",yaxis_title="Voters Count")


tab_1_layout_perth_positive = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_positive_p,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_p),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

tab_1_layout_perth_negative = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_negative_p,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_p),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

#Sydney
twitter_positive_coalition_s =  go.Scatter(x=year,y=de.positive_coalition("Sydney"), name = "Coalition")
twitter_positive_labor_s =  go.Scatter(x=year,y=de.positive_labor("Sydney"), name="Labor")
positive_s = [twitter_positive_coalition_s , twitter_positive_labor_s ]
fig_positive_s = go.Figure(data=positive_s, layout=layout)
fig_positive_s.update_layout(xaxis_title="Year",yaxis_title="Percentage")


twitter_negative_coalition_s = go.Scatter(x=year,y=de.negative_coalition("Sydney"), name = "Coalition")
twitter_negative_labor_s = go.Scatter(x=year,y=de.negative_labor("Sydney"), name = "Labor")
negative_s = [twitter_negative_coalition_s,twitter_negative_labor_s]
fig_negative_s = go.Figure(data=negative_s, layout=layout)
fig_negative_s.update_layout(xaxis_title="Year",yaxis_title="Percentage")

aurin_data_2016_s = go.Bar(x=[2016,2019],y=de.aurinPartyData2016("Sydney"),name="Coalition")
aurin_data_2019_s = go.Bar(x=[2016,2019],y=de.aurinPartyData2019("Sydney"),name = "Labor")
fig_aurin_s = go.Figure(data=[aurin_data_2016_s,aurin_data_2019_s])
fig_aurin_s.update_layout(barmode='group',xaxis_title="Year",yaxis_title="Voters Count")


tab_1_layout_sydney_positive = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_positive_s,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_s),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

tab_1_layout_sydney_negative = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_negative_s,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_s),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

#Australia
twitter_positive_coalition_aus =  go.Scatter(x=year,y=de.positive_coalition("australia"), name = "Coalition")
twitter_positive_labor_aus =  go.Scatter(x=year,y=de.positive_labor("australia"), name="Labor")
positive_aus = [twitter_positive_coalition_aus , twitter_positive_labor_aus ]
fig_positive_aus = go.Figure(data=positive_aus, layout=layout)
fig_positive_aus.update_layout(xaxis_title="Year",yaxis_title="Percentage")


twitter_negative_coalition_aus = go.Scatter(x=year,y=de.negative_coalition("australia"), name = "Coalition")
twitter_negative_labor_aus = go.Scatter(x=year,y=de.negative_labor("australia"), name = "Labor")
negative_aus = [twitter_negative_coalition_aus,twitter_negative_labor_aus]
fig_negative_aus = go.Figure(data=negative_aus, layout=layout)
fig_negative_aus.update_layout(xaxis_title="Year",yaxis_title="Percentage")

aurin_data_2016_aus = go.Bar(x=[2016,2019],y=de.aurin2016Australia(),name="Coalition")
aurin_data_2019_aus = go.Bar(x=[2016,2019],y=de.aurin2019Australia(),name = "Labor")
fig_aurin_aus = go.Figure(data=[aurin_data_2016_aus,aurin_data_2019_aus])
fig_aurin_aus.update_layout(barmode='group',xaxis_title="Year",yaxis_title="Voters Count")


tab_1_layout_australia_positive = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_positive_aus,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_aus),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])

tab_1_layout_australia_negative = html.Div([
    html.Div([
        html.H3('Sentiment of tweets for across years',style={
            'textAlign': 'center'}
        ),
        dcc.Graph(id='graph',
                  figure=fig_negative_aus,
                  style={'padding-right': '1px'}
                  )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([

        html.H3('Election results', style={
            'textAlign': 'center',
        }),
        dcc.Graph(id='graph1',
                  figure=fig_aurin_aus),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='page-1-content')
])



