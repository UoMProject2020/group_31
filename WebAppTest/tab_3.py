import plotly_express as px
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

df = px.data.iris()

tab_3_layout = html.Div([
    html.H3('IRIS'),
    dcc.Graph(id='iris',
              figure=px.density_heatmap(df, x="sepal_width", y="sepal_length", marginal_x="rug",
                                        marginal_y="histogram")),
    html.Div(id='page-2-content')
])
