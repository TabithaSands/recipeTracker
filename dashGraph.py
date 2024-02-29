from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.year.unique(), '2000', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    # dff = df[df.country == value]
    d1 = df["continent"]
    d2 = df["country"]
    d3 = df[df["year"] == value]
    d4 = d3["pop"]
    data = dict(
        c = d1
    )
    return px.sunburst(data)
    # return px.bar(dff, x='year', y='pop')
    # return px.line(dff, x='year', y='pop')


if __name__ == '__main__':
    app.run(debug=True)
