#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 01:03:27 2018

@author: gaurav
"""

#remove imogies
import re

text = u'This dog \U0001f602'
print(text) # with emoji

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
print(emoji_pattern.sub(r'', text)) # no emoji






#an;other

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)











import pandas as pd

filepath = 'labeled_dataset/clean_tweet/clean_tweets.csv'
df = pd.read_csv(filepath)

df.columns

for row in df.itertuples(index=True, name='Pandas'):
    tweet = getattr(row, "tweet")
    tweet_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",tweet).split())

    tw = ''
    for i in tweet_n:
        tw = tw + ' ' + i 


    row['cleaned_tweet'] = tw

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:07:05 2018

@author: gaurav
"""

"""
import pandas as pd

filePath = 'datasets/labeled_dataset/processed_data.csv'
df = pd.read_csv(filePath, usecols=['sentiment_value','tweet'])

df['sentiment_value'].astype(str).astype(int)

newFilePath = 'datsets/labeled_dataset/labeled_tweets.csv'
df.to_csv(newFilePath, index=False)

"""

"""
import csv
import re

def clean_Tweet(tweet):
    tweet_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",tweet).split())

    tw = ''
    for i in tweet_n:
        tw = tw + ' ' + i
        
    return tw


file_w = open('final.csv','w')
writer = csv.DictWriter(file_w, delimiter=',', fieldnames=["sentiment_value","tweet"])
with open('sentiment_tweet.csv', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sentiment_value = row['sentiment_value']
        tweet = row['tweet']
        tweet = clean_Tweet(tweet)
        new_row = {'sentiment_value' :sentiment_value ,'tweet': tweet}
        writer.writerow(new_row)
        
"""