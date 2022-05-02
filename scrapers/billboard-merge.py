import pandas as pd

df = pd.read_csv('billboard-df.csv')
df.drop(df.columns[[0, 1]], axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
df.sort_values(by=['date', 'track_rank'], inplace=True)
global tracks
tracks = [df['track_title']]
df.to_csv('billboard-df.csv', index=False)
