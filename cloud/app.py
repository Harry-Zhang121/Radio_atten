from dash import Dash, html, dcc, Input, Output, State, ctx
import plotly.express as px
import cx_Oracle
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
import config

colors = {
    'background': '#e5ecf6',
    'text': '#7FDBFF'
}

# Initialize Oracle database client
# cx_Oracle.init_oracle_client(r"C:\Users\harry\Documents\Radio_atten\ignore\instantclient_21_7")

# Read user credentials from config file
user = config.oracle["user"]
password = config.oracle["password"]
dsn = config.oracle["dsn"]

engine = create_engine(
    f'oracle://{user}:{password}@{dsn}/?encoding=UTF-8&nencoding=UTF-8', max_identifier_length=128)

connection = engine.connect()



# Assamble datetime string used for sql query based on current and a timedelta.
def get_datetime_by_duration(delta):
    current_time = datetime.now()
    start_time = current_time - timedelta(hours=delta)
    start_time_str = start_time.strftime(r"%H:%M:%S %Y-%m-%d")
    end_time_str = current_time.strftime(r"%H:%M:%S %Y-%m-%d")
    return [start_time_str, end_time_str]

# Assamble datetime string used for sql query based on start date and end date.
def get_datetime_by_date(start_date, end_date):
    start_date_str = "00:00:00 {}".format(start_date)
    end_date_str = "12:59:59 {}".format(end_date)
    return [start_date_str, end_date_str]



# Dash app
app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': colors['background']}, 
children=[
    html.H1(style={"text-align": "center"}, children='Radio signal data'),
    dcc.Graph(id="output-graph"),
    

    html.Div(style = {"float": "left"}, children=[
        html.Div(style = {"display": "inline-block"}, children=[
            html.P("Input hours:"),
            dcc.Input(id='input-hours', type='number', min=0, max=72, debounce=True, placeholder="recent n hours"),
            html.Button('Submit', id='btn-recent-hours', n_clicks=0, className="button")
        ]),

        html.Div(style = {"width": "900px"}, children=[
            html.P("Select time period:"),
            dcc.DatePickerRange(
                id='date-picker-range',
                min_date_allowed="2022-10-01",
                max_date_allowed="2024-12-31",
                initial_visible_month="2022-11-04",
                start_date="2022-11-04",
                end_date="2022-11-05"
            ),
            html.Button('Submit_date', id='btn-date-range', n_clicks=0)
        ])
    ])   
])


@app.callback(
    Output('output-graph', 'figure'),
    Input('btn-recent-hours', 'n_clicks'),
    Input('btn-date-range', 'n_clicks'),
    State('date-picker-range', 'start_date'),
    State('date-picker-range', 'end_date'),
    State('input-hours','value'))
def update_output(btn1, btn2, start_date, end_date, value):
    # By default display the last 5 hours of data
    query_date_str = get_datetime_by_duration(5)
    # If user want last n hours of data
    if "btn-recent-hours" == ctx.triggered_id:
        query_date_str = get_datetime_by_duration(value)
    # If user want to specify start and end date
    elif "btn-date-range" == ctx.triggered_id:
        query_date_str = get_datetime_by_date(start_date, end_date)

    # Assamble query command
    query = '''
            select * from DATA
            where TIMESTAMP
            between to_timestamp('{}', 'HH24:MI:SS YYYY-MM-DD')
            and to_timestamp('{}', 'HH24:MI:SS YYYY-MM-DD')
            order by TIMESTAMP ASC
    '''.format(query_date_str[0], query_date_str[1])

    # Store data from database query to pandas datafram
    datafram = pd.read_sql_query(query, connection)

    # Prepare the figure
    fig = px.line(datafram, x="timestamp", y=["e_level","v_level"])
    return fig

if __name__ == '__main__':
    app.run_server(host= '0.0.0.0', debug=True)
