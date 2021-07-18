import IAQIndex
import VisualizeIAQData
import pandas as pd

in_file = 'iaq_hour_dummy_dataset.csv'
IAQdata = pd.read_csv(in_file, parse_dates=True, index_col='create_time', date_parser=VisualizeIAQData.dateparse)

col = []

for it in IAQdata['pm2.5']:
    col.append(IAQIndex.HealthLevel(IAQIndex.AirQualityIndex('PM2.5', it)))

IAQdata['health level'] = col
IAQdata[['pm2.5', 'temperature', 'humidity', 'health level']].to_csv('IAQData.txt', sep='\t')
