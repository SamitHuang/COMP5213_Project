
import plotly

# Authenticate with your account
plotly.tools.set_credentials_file(username='mariachen03',                                              
                                  api_key='8aKflxzhUtqcimZ4Pu02')

import plotly.plotly as py
import plotly.graph_objs as go

# Offline mode
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)


import pandas as pd

# Read in data
df = pd.read_csv('run_.-tag-episode success indicator.csv', header=0, index_col=1)

# Extract value series from multi-index
value_series = df.loc[:, 'Value']

success_rate = go.Scatter(x=value_series.index,
                         y=value_series.values)

layout = go.Layout(title='episode_success_indicator', xaxis=dict(title='Episode'),
                   yaxis=dict(title='Success Ratio'))

fig = go.Figure(data=[success_rate], layout=layout)
py.iplot(fig)                   