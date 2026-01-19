#10a
import plotly.graph_objects as go
import pandas as pd
dates = pd.date_range(start='2024-01-01', end='2024-01-10')
values = [5, 7, 9, 10, 8, 6, 4, 3, 5, 7]
data = pd.DataFrame({
    'Date': dates,
    'Value': values
})
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data['Date'],
        y=data['Value'],
        mode='lines',
        name='Time Series'
    )
)
fig.update_layout(
    title='Time Series Plot using Plotly',
    xaxis_title='Date',
    yaxis_title='Value'
)
fig.show()

#10b
import plotly.graph_objects as go
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
latitudes = [40.7128, 34.0522, 41.8781, 29.7604, 33.4484]
longitudes = [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740]
populations = [8398748, 3990456, 2705994, 2325502, 1680992]
fig = go.Figure()
fig.add_trace(
    go.Scattergeo(
        lon=longitudes,
        lat=latitudes,
        text=cities,
        mode='markers',
        marker=dict(
            size=[pop / 100000 for pop in populations],  # scale marker size
            color='rgb(255, 0, 0)',
            line=dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        )
    )
)
fig.update_layout(
    title='Cities Population Map',
    geo=dict(
        scope='usa',
        showland=True
    )
)
fig.show()
