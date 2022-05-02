import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

rows = []
headers = ['year', 'track rank', 'track name', 'track artist']

for i in range(1920, 2017):
    url = ('https://playback.fm/charts/top-100-songs/{}'.format(i))
    print('Scraping... ' + url)
    result = req.get(url)
    soup = bs(result.content, 'html.parser')

    
    table = soup.find('table', {'id':'myTable'})

    for tr in table.find_all("tr")[1:]:
        cells = []
        year = i
        track_rank = tr.find('td').text
        track_name = tr.find('a', {'itemprop':'name'}).text.replace('\n', '')
        track_artist = tr.find('a', {'class':'artist'}).text.replace('\n', '')
        cells = [i] + [track_rank] + [track_name] + [track_artist]
        rows.append(cells)
df = pd.DataFrame(rows, columns=headers)
df.to_csv('playbackfm-1920-2016.csv', index=False)