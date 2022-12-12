import dash
import dash_core_components as dcc
import dash_html_components as html

# Create a dictionary with dummy radio signal data
radio_signal_data = {
    'AM': [1, 2, 3, 4, 5],
    'FM': [5, 6, 7, 8, 9],
    'SW': [9, 8, 7, 6, 5]
}

# Create the Dash app
app = dash.Dash()

# Define the app layout
app.layout = html.Div([
    html.H1('Radio Signal Monitor'),
    dcc.Dropdown(
        id='radio-signal-dropdown',
        options=[
            {'label': 'AM', 'value': 'AM'},
            {'label': 'FM', 'value': 'FM'},
            {'label': 'SW', 'value': 'SW'},
        ],
        value='AM'
    ),
    dcc.Graph(
        id='radio-signal-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': radio_signal_data['AM'], 'type': 'line', 'name': 'AM'},
                {'x': [1, 2, 3, 4, 5], 'y': radio_signal_data['FM'], 'type': 'line', 'name': 'FM'},
                {'x': [1, 2, 3, 4, 5], 'y': radio_signal_data['SW'], 'type': 'line', 'name': 'SW'},
            ],
            'layout': {
                'title': 'Radio Signal Data'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()
