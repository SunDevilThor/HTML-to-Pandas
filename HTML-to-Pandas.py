# Using Pandas to Scrape Tables from HTML
# Tutorial from John Watson Rooney YouTube channel

import pandas as pd

df = pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti')

# print(df[0])

# You can use skiprows= and specify a number to skip those rows

df2 = pd.read_html('https://en.wikipedia.org/wiki/Land_speed_record', parse_dates=True)

df2[0].to_csv('Land-speed-record.csv')
print('Items saved to CSV file.')

# NOTES: 
# Really good for scraping tables from Wikipedia