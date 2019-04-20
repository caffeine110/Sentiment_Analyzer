#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
        Tweet exctraction
        input:

"""

import tweepy
import csv
import pandas as pd


consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('hashtag_TrumpLies.csv', 'a')


# q = @twitterHandler
# q = #hashtag
# lan='en'
# since = From the date


csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search, q="#TrumpLies", count=300, lang="en", since="2019-03-03").items():

    print (tweet.created_at, tweet.text, )
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
