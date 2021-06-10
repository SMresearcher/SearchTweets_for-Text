# Import the Twython class
from twython import Twython
import json
import pandas as pd
import csv

# Load credentials from json file
with open("mytwitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])


# querytext='#supermoon'
#data=python_tweets.search(q=querytext,count=5, lang='en')
querytext="covid"
data=python_tweets.search(q=querytext, result_type='popular',count=50, lang='en')


dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in data['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

pd.set_option('display.max_columns', 4)
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count',  ascending=False)
print(df.head(5))
print(df)
df.to_csv(querytext+ ".csv", index=False, mode='a')

