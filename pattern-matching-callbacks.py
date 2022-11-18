from dash import Dash, dcc, html, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

app = Dash(__name__, suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    html.Button("Add Filter", id="add-filter", n_clicks=0),
    html.Div(id='dropdown-container', children=[]),
    html.Div(id='dropdown-container-output')
])

# Add Filter button callback
@app.callback(
    # Output container with dropdowns
    Output('dropdown-container', 'children'),
    # Input num of clicks (use as trigger)
    Input('add-filter', 'n_clicks'),
    # Input current container state (no trigger)
    State('dropdown-container', 'children'))
def display_dropdowns(n_clicks, children):
    new_dropdown = dcc.Dropdown(
        ['NYC', 'MTL', 'LA', 'TOKYO'],
        id={
            'type': 'filter-dropdown',
            'index': n_clicks
        }
    )
    children.append(new_dropdown)
    return children

@app.callback(
    Output('dropdown-container-output', 'children'),
    # Filter dropdowns by MATCH, taking the value of the modified indexes
    Input({'type': 'filter-dropdown', 'index': ALL}, 'value')
)
def display_output(values):
    return html.Div([
        html.Div('Dropdown {} = {}'.format(i + 1, value))
        for (i, value) in enumerate(values)
    ])


if __name__ == '__main__':
    app.run_server(debug=True)