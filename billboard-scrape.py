from timeit import timeit
import billboard
import pandas as pd
from time import sleep

rows = []
headers = ['year', 'track rank', 'track name', 'track artist']

print('December')

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

sleep(0.05)

print('November')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-11-30".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('October')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-10-31".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('September')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-9-30".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('August')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-8-31".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('July')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-7-31".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('June')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-6-30".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('May')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-5-31".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('April')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-4-30".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('March')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-3-31".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('February')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-2-29".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)

sleep(0.05)

print('January')

for year in range(1960, 2022):
    chart = []
    print("Scraping year {}".format(year))
    chart = billboard.ChartData('hot-100', date="{}-1-31".format(year))
    for i in range (0, 49):
        cells = []
        entry = chart[i]
        track_title = entry.title
        track_artist = entry.artist
        track_rank = entry.rank
        cells = [year] + [track_rank] + [track_title] + [track_artist]
        rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)



print('Complete')

df.to_excel('billboard-1960-2022.xlsx', index=False)