#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
"""


"""
tweet_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
tw = ''
for i in tweet_n:
tw = tw + ' ' + i 
print(tw)

analysis = TextBlob(tw)
"""


from textblob import TextBlob
import pandas as pd
import numpy as np
import os
import re

field_names = ['sentiment_value', 'id', 'date_and_time', 'query', 'tweet']



class PreProcessor(object):
    def __init__ (self,df):
        self.df = df


    def remove_Duplicates(self,df):
        df.drop_duplicates(inplace=True)

    def change_Column_Names(self,df):
        df.columns = ['sentiment_value','tweet']


    def remove_NaN(self,df):        
        df['sentiment_value'].fillna('Unknown', inplace=True)
        df['tweet'].fillna('Unknown', inplace=True)
        
        
    def clean_Tweets(self,df):
        try:
            tweet_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", df['tweet'].text).split())
            tw = ''
            for i in tweet_n:
                tw = tw + ' ' + i 
                print(tw)
                
        except:
            return 'this is neutral'
        
        return df


    def sentiment_To_Int(self,df):
        df['sentiment_value'].astype(str).astype(int)

        
    def get_Details(self,df):
        print(df.count)
        print(df.info)
        print(df.dtypes)
        print(df.columns)



    def to_new_CSV(self,df):
        newFilePath = 'labeled_dataset/clean_tweet/clean_tweets.csv'
        df.to_csv(newFilePath, index= False)
        
        
        
def main():

    filepath = 'labeled_dataset/preprocessing/processed_data.csv'
    df = pd.read_csv(filepath, usecols=['sentiment_value','tweet'])
    print(df.count)


    #initialising object    
    api = PreProcessor(df)

    #calling functinos
    api.remove_Duplicates(df)
    api.change_Column_Names(df)
    api.remove_NaN(df)
    api.clean_Tweets(df)
    api.sentiment_To_Int(df)
    #api.get_Details(df)
    api.to_new_CSV(df)


if __name__ == "__main__":
    #calling main function
    main()