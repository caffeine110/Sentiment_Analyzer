#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
    
Aim     : To read downloaded file using proper encodeing
        : To remove NaN
        : To Exctract importent data
        
        : input file  <<  ...phase_2_exctraion/sentiment_tweet.csv
        : output file <<  ...phase_3_cleaning/clean_sentiment_tweet.csv
"""



###############################################################################
# importing
from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup
import pandas as pd
import re


###############################################################################
def getDetails(df):
    # show metadata
    print(df.head())
    print(df.tail())
    print(df.count)
    print(df.columns)
    print(df['sentiment_value'].head())
    print(df['tweet'].head())


###############################################################################
# function to clean the tweet
def tweet_Cleaner(text):
    soup = BeautifulSoup(text, 'lxml')
    souped = soup.get_text()
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    # During the letters_only process two lines above, it has created unnecessay white spaces,
    # I will tokenize and join together to remove unneccessary white spaces
    words = tok.tokenize(lower_case)

    return (" ".join(words)).strip()




###############################################################################
# read file and df
filePath_o = 'phase_2_exctraction/sentiment_tweet.csv'
df = pd.read_csv(filePath_o, encoding = 'utf8')

tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))


###############################################################################
# apply the funciton to the df
for index, row in df.iterrows():
    sentiment_value = row['sentiment_value']
    tweet = row['tweet']

    clean_tweet = tweet_Cleaner(tweet)
    clean_tweet.strip()

    df.sentiment_value[index] = sentiment_value
    df.tweet[index] = clean_tweet
    print(index)





###############################################################################
# write df into file
filePath_w = 'phase_3_cleaning/clean_sentiment_tweet.csv'
df.to_csv(filePath_w, index = False)

