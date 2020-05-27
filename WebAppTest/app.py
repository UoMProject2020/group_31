#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

import tab_1
import tab_2
import tab_3
import os

host = os.getenv('host')

app = dash.Dash()

app.config[ 'suppress_callback_exceptions' ] = True

tabs_styles = {
    'height': '50px',
    'padding': '10px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold',
    'text-align': 'center'
}

tab_selected_style = {
    'backgroundColor': '#e8e6e6',
    'color': 'black',
    'text-align': 'center'
}

app.layout = html.Div([
    html.H1('Are All Battles Won In Battlefield???',
            style=dict(textAlign='center')),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Do engagement reflect votes?', value='tab-1-example', style=tab_style, selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.P('Is there a correlation between political tweets related to parties and election results e.g. increase in number of positive tweets or decrease '
                               'in negative tweets for a party, so we might expect that party to win the election?')
                    ],style={'font-size':'20px'}),
                    html.Div([
                        html.H3("""City: """,
                                style={'height': '50px',
                                       'padding': '10px',
                                       'float': 'left',
                                       'margin': 'auto'}),
                        dcc.Dropdown(
                            id='city_dropdown_1',
                            options=[
                                {'label': 'Australia', 'value': 'australia'},
                                {'label': 'Melbourne', 'value': 'melbourne'},
                                {'label': 'Sydney', 'value': 'sydney'},
                                {'label': 'Brisbane', 'value': 'brisbane'},
                                {'label': 'Perth', 'value': 'perth'},
                                {'label': 'Adelaide', 'value': 'adelaide'}
                            ],
                            placeholder="Select--",
                            style=dict(
                                width='60%',
                                verticalAlign="middle",
                                display='inline',
                                float='left',
                                margin='auto'
                            ),
                        ), ], style={'float': 'left', 'width': '49%', 'margin-right': '2%'}),
                    html.Div([
                        html.H3("""Sentiment: """,
                                style={'height': '50px',
                                       'padding': '10px',
                                       'display': 'inline',
                                       'float': 'left',
                                       'margin': 'auto'}),
                        dcc.Dropdown(
                            id='party_dropdown_1',
                            options=[
                                {'label': 'Positive', 'value': 'positive'},
                                {'label': 'Negative', 'value': 'negative'},
                            ],
                            placeholder="Select--",
                            style=dict(
                                width='60%',
                                verticalAlign="middle",
                                display='inline',
                                float='left',
                                margin='auto'
                            ))
                    ], style={'float': 'left', 'width': '49%', 'margin-right': '0',
                              'display': 'inline'})
                ]),
        dcc.Tab(label='Compulsion or Interest?', value='tab-2-example', style=tab_style, selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.P('Which city has the most tweeters who tweet on Australian politics and does this correlate with number of voters in that area, e.g. more people with right to vote live in a given area so we might expect more political tweets from that area (assuming people who have right to vote show interest in politics)?')
                    ],style={'font-size':'20px'})
                ]),
        dcc.Tab(label='Youth and Social media', value='tab-3-example', style=tab_style, selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.P('Which city has the most tweeters and does this correlate with what we might from the population demographic of the city from AURIN, e.g. more young people live in a given area so we might expect a proportionate increase in the number of tweets (assuming youth tweet more)?')
                    ],style={'font-size':'20px'})
                ])
    ], style=tabs_styles),

    html.Div(id='tabs-content-1'),
    html.Div(id='tabs-content-2'),
    html.Div(id='tabs-content-3'),
], style={"background": 'white'})


@app.callback(Output('tabs-content-1', 'children'),
              [ Input('tabs-example', 'value'), Input('city_dropdown_1', 'value'), Input('party_dropdown_1', 'value') ])
def render_content(tab, city, party):
    if tab == 'tab-1-example' and city == 'sydney' and party == 'positive':
        return tab_1.tab_1_layout_sydney_positive
    elif tab == 'tab-1-example' and city == 'sydney' and party == 'negative':
        return tab_1.tab_1_layout_sydney_negative
    elif tab == 'tab-1-example' and city == 'adelaide' and party == 'positive':
        return tab_1.tab_1_layout_adelaide_positive
    elif tab == 'tab-1-example' and city == 'adelaide' and party == 'negative':
        return tab_1.tab_1_layout_adelaide_negative
    elif tab == 'tab-1-example' and city == 'melbourne' and party == 'positive':
        return tab_1.tab_1_layout_melbourne_positive
    elif tab == 'tab-1-example' and city == 'melbourne' and party == 'negative':
        return tab_1.tab_1_layout_melbourne_negative
    elif tab == 'tab-1-example' and city == 'perth' and party == 'positive':
        return tab_1.tab_1_layout_perth_positive
    elif tab == 'tab-1-example' and city == 'perth' and party == 'negative':
        return tab_1.tab_1_layout_perth_negative
    elif tab == 'tab-1-example' and city == 'brisbane' and party == 'positive':
        return tab_1.tab_1_layout_brisbane_positive
    elif tab == 'tab-1-example' and city == 'brisbane' and party == 'negative':
        return tab_1.tab_1_layout_brisbane_negative
    elif tab == 'tab-1-example' and city == 'australia' and party == 'positive':
        return tab_1.tab_1_layout_australia_positive
    elif tab == 'tab-1-example' and city == 'australia' and party == 'negative':
        return tab_1.tab_1_layout_australia_negative


@app.callback(Output('tabs-content-2', 'children'),
              [ Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-2-example':
        return tab_2.tab_2_layout

@app.callback(Output('tabs-content-3', 'children'),
              [ Input('tabs-example', 'value') ])
def render_content(tab):
    if tab == 'tab-3-example':
        return tab_3.tab_3_layout

if __name__ == '__main__':
    app.run_server(debug=True,host=host,port=8050)
