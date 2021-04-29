import pandas as pd 

import plotly.express as px 

df = pd.read_csv("data.csv")

fig1 = px.scatter(df,x = 'date', y = 'cases',  color = 'country')

fig1.show()
