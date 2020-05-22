import plotly_express as px
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

df = px.data.gapminder().query("year == 2007")
fig = px.scatter_geo(df, locations="iso_alpha",
                     size="pop", # size of markers, "pop" is one of the columns of gapminder
                     )

tab_3_layout = html.Div([
    html.H3('IRIS'),
    dcc.Graph(id='iris',
              figure=fig),
    html.Div(id='page-2-content')
])
