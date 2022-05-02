import billboard
import pandas as pd
from time import sleep

class billscrapes:
    def __init__(self):
        self.chart = chart = []
        self.rows = rows = []
        self.headers = headers = []

    def create_december_dataset():
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        print('December')
        for year in range(1960, 2022):
            date = "{}-12-31".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df = pd.DataFrame(rows, columns=headers)
        df.to_excel('billboard-dec1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-12-24".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df1 = pd.DataFrame(rows, columns=headers)
        df1.to_excel('billboard-dec2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-12-17".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df2 = pd.DataFrame(rows, columns=headers)
        df2.to_excel('billboard-dec3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-12-10".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df3 = pd.DataFrame(rows, columns=headers)
        df3.to_excel('billboard-dec4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-12-03".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df4 = pd.DataFrame(rows, columns=headers)
        df4.to_excel('billboard-dec5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_november_dataset():
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        print('November')
        for year in range(1960, 2022):
            date = "{}-11-30".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df5 = pd.DataFrame(rows, columns=headers)
        df5.to_excel('billboard-nov1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-11-23".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df6 = pd.DataFrame(rows, columns=headers)
        df6.to_excel('billboard-nov2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-11-16".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df7 = pd.DataFrame(rows, columns=headers)
        df7.to_excel('billboard-nov3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-11-09".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df8 = pd.DataFrame(rows, columns=headers)
        df8.to_excel('billboard-nov4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-11-02".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df9 = pd.DataFrame(rows, columns=headers)
        df9.to_excel('billboard-nov5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_october_dataset():
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        print('October')
        for year in range(1960, 2022):
            date = "{}-10-31".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df10 = pd.DataFrame(rows, columns=headers)
        df10.to_excel('billboard-oct1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-10-24".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df11 = pd.DataFrame(rows, columns=headers)
        df11.to_excel('billboard-oct2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-10-17".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df12 = pd.DataFrame(rows, columns=headers)
        df12.to_excel('billboard-oct3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-10-10".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df13 = pd.DataFrame(rows, columns=headers)
        df13.to_excel('billboard-oct4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-10-03".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df14 = pd.DataFrame(rows, columns=headers)
        df14.to_excel('billboard-oct5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_september_dataset():
        print('September')
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-09-30".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df15 = pd.DataFrame(rows, columns=headers)
        df15.to_excel('billboard-sept1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-09-23".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df16 = pd.DataFrame(rows, columns=headers)
        df16.to_excel('billboard-sept2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-09-16".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df17 = pd.DataFrame(rows, columns=headers)
        df17.to_excel('billboard-sept3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-09-09".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df18 = pd.DataFrame(rows, columns=headers)
        df18.to_excel('billboard-sept4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-09-02".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df19 = pd.DataFrame(rows, columns=headers)
        df19.to_excel('billboard-sept5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_august_dataset():
        print('August')
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-08-31".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df20 = pd.DataFrame(rows, columns=headers)
        df20.to_excel('billboard-aug1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-08-24".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df21 = pd.DataFrame(rows, columns=headers)
        df21.to_excel('billboard-aug2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-08-17".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df22 = pd.DataFrame(rows, columns=headers)
        df22.to_excel('billboard-aug3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-08-10".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df23 = pd.DataFrame(rows, columns=headers)
        df23.to_excel('billboard-aug4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-08-03".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df24 = pd.DataFrame(rows, columns=headers)
        df24.to_excel('billboard-aug5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_july_dataset():
        print('July')
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-07-31".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df25 = pd.DataFrame(rows, columns=headers)
        df25.to_excel('billboard-jul1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-07-24".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df26 = pd.DataFrame(rows, columns=headers)
        df26.to_excel('billboard-jul2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-07-17".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df27 = pd.DataFrame(rows, columns=headers)
        df27.to_excel('billboard-jul3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-07-10".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df28 = pd.DataFrame(rows, columns=headers)
        df28.to_excel('billboard-jul4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-07-03".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df29 = pd.DataFrame(rows, columns=headers)
        df29.to_excel('billboard-jul5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_june_dataset():
        print('June')
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-06-30".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df30 = pd.DataFrame(rows, columns=headers)
        df30.to_excel('billboard-jun1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-06-23".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df31 = pd.DataFrame(rows, columns=headers)
        df31.to_excel('billboard-jun2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-06-16".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df32 = pd.DataFrame(rows, columns=headers)
        df32.to_excel('billboard-jun3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-06-09".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_title = entry.title
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df33 = pd.DataFrame(rows, columns=headers)
        df33.to_excel('billboard-jun4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-06-02".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df34 = pd.DataFrame(rows, columns=headers)
        df34.to_excel('billboard-jun5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_may_dataset():
        print('May')
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-05-31".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df35 = pd.DataFrame(rows, columns=headers)
        df35.to_excel('billboard-may1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-05-24".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df36 = pd.DataFrame(rows, columns=headers)
        df36.to_excel('billboard-may2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-05-17".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df37 = pd.DataFrame(rows, columns=headers)
        df37.to_excel('billboard-may3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-05-10".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df38 = pd.DataFrame(rows, columns=headers)
        df38.to_excel('billboard-may4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-05-03".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df39 = pd.DataFrame(rows, columns=headers)
        df39.to_excel('billboard-may5-1960-2022.xlsx', index=False)
        sleep(0.05)
        

    def create_april_dataset():
        print('April')
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-04-30".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df40 = pd.DataFrame(rows, columns=headers)
        df40.to_excel('billboard-apr1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-04-23".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df41 = pd.DataFrame(rows, columns=headers)
        df41.to_excel('billboard-apr2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-04-16".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df42 = pd.DataFrame(rows, columns=headers)
        df42.to_excel('billboard-apr3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-04-09".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df43 = pd.DataFrame(rows, columns=headers)
        df43.to_excel('billboard-apr4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-04-02".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df45 = pd.DataFrame(rows, columns=headers)
        df45.to_excel('billboard-apr5-1960-2022.xlsx', index=False)
        sleep(0.05)
        

    def create_march_dataset():
        print('March')
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-03-31".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df46 = pd.DataFrame(rows, columns=headers)
        df46.to_excel('billboard-mar1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-03-24".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df47 = pd.DataFrame(rows, columns=headers)
        df47.to_excel('billboard-mar2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-03-17".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df48 = pd.DataFrame(rows, columns=headers)
        df48.to_excel('billboard-mar3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-03-10".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df49 = pd.DataFrame(rows, columns=headers)
        df49.to_excel('billboard-mar4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-03-03".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df50 = pd.DataFrame(rows, columns=headers)
        df50.to_excel('billboard-mar5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_february_dataset():
        print('February')
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-02-28".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df51 = pd.DataFrame(rows, columns=headers)
        df51.to_excel('billboard-feb1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-02-21".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df52 = pd.DataFrame(rows, columns=headers)
        df52.to_excel('billboard-feb2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-02-14".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df53 = pd.DataFrame(rows, columns=headers)
        df53.to_excel('billboard-feb3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-02-07".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df54 = pd.DataFrame(rows, columns=headers)
        df54.to_excel('billboard-feb4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-02-01".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df55 = pd.DataFrame(rows, columns=headers)
        df55.to_excel('billboard-feb5-1960-2022.xlsx', index=False)
        sleep(0.05)

    def create_january_dataset():
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        print('January')
        for year in range(1960, 2022):
            date = "{}-01-31".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df56 = pd.DataFrame(rows, columns=headers)
        df56.to_excel('billboard-jan1-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-01-24".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df57 = pd.DataFrame(rows, columns=headers)
        df57.to_excel('billboard-jan2-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-01-17".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df58 = pd.DataFrame(rows, columns=headers)
        df58.to_excel('billboard-jan3-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-01-10".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df59 = pd.DataFrame(rows, columns=headers)
        df59.to_excel('billboard-jan4-1960-2022.xlsx', index=False)
        sleep(0.01)
        rows = []
        headers = ['date', 'track_rank', 'track_title', 'track_artist', 'track_weeks', 'track_lp', 'track_pp', 'track_new']
        for year in range(1960, 2022):
            date = "{}-01-03".format(year)
            chart = []
            print("Scraping year {}".format(year))
            chart = billboard.ChartData('hot-100', date=date)
            for i in range (0, 49):
                cells = []
                entry = chart[i]
                track_date = date
                track_weeks = entry.weeks
                track_lp = entry.lastPos
                track_pp = entry.peakPos
                track_new = entry.isNew
                track_title = entry.title
                track_artist = entry.artist
                track_rank = entry.rank
                cells = [track_date] + [track_rank] + [track_title] + [track_artist] + [track_weeks] + [track_lp] + [track_pp] + [track_new]
                rows.append(cells)
                df60 = pd.DataFrame(rows, columns=headers)
        df60.to_excel('billboard-jan5-1960-2022.xlsx', index=False)
        sleep(0.05)
