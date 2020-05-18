import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import tab_1
import tab_2
import tab_3

app = dash.Dash()

app.config['suppress_callback_exceptions'] = True

tabs_styles = {
    'height': '50px',
    'padding': '10px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '2px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'black',
    'color': 'yellow',
    'padding': '10px'
}

app.layout = html.Div([
    html.H1('Test',
            style={
                'textAlign': 'center',
                "background": 'yellow'
            }),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Tab One', value='tab-1-example', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab Two', value='tab-2-example', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab Three', value='tab-3-example', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles,
            colors={
            "border": "yellow",
            "primary": "red",
            "background": "orange"
            }),
    html.Div(id='tabs-content-example')
])


@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-example':
        return tab_2.tab_2_layout
    elif tab == 'tab-2-example':
        return tab_3.tab_3_layout


if __name__ == '__main__':
    app.run_server(debug=True)