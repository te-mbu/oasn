import pandas as pd

# applications json to csv

data_applications = pd.read_json('data_applications.json')
data_applications.to_csv('data_applications.csv')

#trackers json to csv

data_trackers = pd.read_json('data_trackers.json', orient='index')
data_trackers.to_csv('data_trackers.csv', index=False)