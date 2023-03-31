import plotly.express as px
import pandas as pd

df = pd.read_csv("dataset.csv")

fig = px.scatter_geo(df,lat='lat',lon='long', hover_name="id")
fig.update_layout(title = 'World map', title_x=0.5)
fig.show()