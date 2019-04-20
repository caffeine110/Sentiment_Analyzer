#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:21:55 2019

@author: gaurav
"""




import pandas as pd

df = pd.read_csv('cleaned_sentiment_tweet.csv')
print(df.columns)

file = open('stopwords_eng.txt', 'r')

lines = file.readlines()

print(lines)

stopwords = list()

for l in lines:
    l = l.replace('\n','')
    l = l.strip()
    stopwords.append(l)

print(stopwords)

for s in stopwords:
    print('for : ', s)
    df['tweeet'] = df['tweet'].replace(s,' ')


filePath = 'rmstop_cleaned_sentiment_tweet.csv'

print(df['tweet'].head())


