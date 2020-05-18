import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

gapminder = px.data.gapminder()

dimensions = []


external_stylesheets = [ 'https://codepen.io/chriddyp/pen/bWLwgP.css 5' ]
colors = {
    'background': '#111111',
    'background2': '#FF0',
    'text': '#7FDBFF'
}

tab_2_layout = html.Div([
    html.H1("Gapminder data"),
    dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"},
              figure=px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year",
                                animation_group="country",
                                size="pop", color="continent", hover_name="country",
                                log_x=True, size_max=55, range_x=[ 100, 100000 ], range_y=[ 25, 90 ])),
])
