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
tok = WordPunctTokenizer()
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
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
    try:
        bom_removed = souped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        bom_removed = souped
    stripped = re.sub(combined_pat, '', bom_removed)
    stripped = re.sub(www_pat, '', stripped)
    lower_case = stripped.lower()
    neg_handled = neg_pattern.sub(lambda x: negations_dic[x.group()], lower_case)
    letters_only = re.sub("[^a-zA-Z]", " ", neg_handled)
    # During the letters_only process two lines above, it has created unnecessay white spaces,
    # I will tokenize and join together to remove unneccessary white spaces
    words = [x for x  in tok.tokenize(letters_only) if len(x) > 1]
    return (" ".join(words)).strip()



###############################################################################
# read file and df
filePath_o = 'phase_2_exctraction/sentiment_tweet.csv'
df = pd.read_csv(filePath_o, encoding = 'utf8')

pat1 = r'@[A-Za-z0-9_]+'
pat2 = r'https?://[^ ]+'
combined_pat = r'|'.join((pat1, pat2))
www_pat = r'www.[^ ]+'
negations_dic = {"isn't":"is not", "aren't":"are not", "wasn't":"was not", "weren't":"were not",
                "haven't":"have not","hasn't":"has not","hadn't":"had not","won't":"will not",
                "wouldn't":"would not", "don't":"do not", "doesn't":"does not","didn't":"did not",
                "can't":"can not","couldn't":"could not","shouldn't":"should not","mightn't":"might not",
                "mustn't":"must not"}
neg_pattern = re.compile(r'\b(' + '|'.join(negations_dic.keys()) + r')\b')




###############################################################################
# apply the funciton to the df
clean_tweet_texts = []
for i in range(0,1599999):
    clean_tweet_texts.append(tweet_Cleaner(df['tweet'][i]))

print(df.head())

clean_df = pd.DataFrame(clean_tweet_texts,columns=['tweet'])
clean_df['sentiment_value'] = df.sentiment_value

clean_df.head()
clean_df.tail()


###############################################################################
clean_df.columns = ['sentiment_value', 'tweet']

# to well organize the df
clean_df['tweet'], clean_df['sentiment_value'] = clean_df['sentiment_value'],clean_df['tweet']


clean_df.head()
clean_df.tail()

#clean_df[clean_df.isnull().any(axis=1)].head()
#np.sum(clean_df.isnull().any(axis=1))

# to drop the empty tweets if any after cleaning
clean_df.dropna(inplace=True)
clean_df.reset_index(drop=True,inplace=True)
clean_df.info()



###############################################################################
# write df into file
filePath_w = 'phase_3_cleaning/clean_sentiment_tweet.csv'
clean_df.to_csv(filePath_w, index = False)

