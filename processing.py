#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:38:27 2018

@author : Gaurav Gahukar
        : caffeine110
Aim : To Filter the Tweets required for Superwise Learning model
    : reading the data from Extrated data set and save it in another file after the processing

"""


#importing all the libraries
import re
from textblob import TextBlob
import pandas as pd

#function to clean tweets
def clean_tweet(tweet):
    try:
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    except:
        return 'this is neutral'


#function to analyse the sentiment value of cleaned tweets
def analize_sentiment(tweet):

    #calling clean_tweet function
    analysis = TextBlob(clean_tweet(tweet))

    try:
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    except:
        return 'neutral'


#main funciton
def main():

    df = pd.read_csv('dataset.csv')
    #change column names
    df.columns = ["DateTime" , "Tweet"]
    #insert new column
    df['SentimentValue']=''

    #for each tweet in dataset.csv 
    for tweet in df['Tweet']:
        
        #get SentimentValue and store
        df['SentimentValue'] = analize_sentiment(tweet)

    #display in case
    #print(df)    

    #to save processed data into processed.csv file
    df.to_csv('processed.csv')
    

 

if"__name__" == "__main__":
    main()
