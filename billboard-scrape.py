import billboard
import pandas as pd

rows = []
headers = ['year', 'track rank', 'track name', 'track artist']


for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-12-31".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)
    

df.to_excel('billboard-1960-2022.xlsx', index=False)