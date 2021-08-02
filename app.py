import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.io as pio
import pandas as pd


# template of plots
pio.templates.default = "plotly_white"

# create app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


# load data
morocco_clusters = pd.read_csv("data.csv")

# construct graph
fig = px.scatter_geo(
    morocco_clusters, 
    lat="lat", lon="lon",
    color="cluster", color_discrete_sequence=['#FFA15A', '#636EFA', "#00CC96"],
    hover_name="city_name", 
    animation_frame="year"
    )

fig.update_layout(
    title = 'Morocco cluster',
    geo=dict(
        showocean=True, 
        oceancolor="rgba(134, 177, 252, 0.2)",
    )
)


# layout of app 
app.layout = html.Div(children=[
    dcc.Graph(
        id='moroccan map',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
