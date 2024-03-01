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
    df["world"] = "world"
    d1 = df[df["continent"] == value]
    d2 = d1[d1["year"] == 2000]
    child = d2["country"].to_list()
    parent = d2["continent"].to_list()

    pop = d2["pop"].to_list()
    data = dict(
        country=child,
        continent=parent,
        population=pop
    )
    return px.sunburst(data,
                       names='country',
                       parents='continent',
                       values='population')
    # return px.bar(dff, x='year', y='pop')
    # return px.line(dff, x='year', y='pop')


if __name__ == '__main__':
    app.run(debug=True)
