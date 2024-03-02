from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
    dcc.Dropdown(df.continent.unique(), 'Asia', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    d1 = df[df["continent"] == value]
    # fig = px.sunburst(d1, path=['continent', 'year', 'country'], values='pop')
    fig = px.sunburst(d1, path=['continent', 'country', 'year'], values='pop')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
