from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

dataset = 'https://raw.githubusercontent.com/howh18170422/render_test/main/waste_data.csv'

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H4('Garbage Collected per year'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=['North East ', 'Grampians Central West ', 'Metropolitan ',
       'Gippsland ', 'Loddon Mallee ', 'Goulburn Valley ',
       'Barwon South West ', 'North East WRRG',
       'Grampians Central West WRRG', 'Metropolitan WRRG',
       'Gippsland WRRG', 'Loddon Mallee WRRG', 'Goulburn Valley WRRG',
       'Barwon South West WRRG'],
        value=['Metropolitan '],
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))

def update_line_chart(regions):
    df = pd.read_csv(dataset)
    mask = df['Waste Resource Recovery Group WRRG'].isin(regions)
    fig = px.line(df[mask], 
        x='Reference Year', y='Garbage Annual Tonnes Collected', color='Local Government')
    return fig

app.run_server(debug=True,use_reloader=False)
