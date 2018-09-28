#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
"""



import csv
import re

def clean_Tweet(tweet):
    tweet_n = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",tweet).split()

    tw = ''
    for i in tweet_n:
        tw = tw + ' ' + i
        
    return tw


def open_Tweet_File():
    file_w = open('labeled_dataset/clean_tweet/clean_tweets.csv', 'w')
    writer = csv.DictWriter(file_w, delimiter=',', fieldnames=["sentiment_value","tweet"])
    with open('labeled_dataset/clean_tweet/sentiment_tweet.csv', newline='') as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            sentiment_value = row['sentiment_value']
            if sentiment_value == '4':
                sentiment_value = '1'
                
            tweet = row['tweet']
            tweet = clean_Tweet(tweet)
            new_row = {'sentiment_value' :sentiment_value ,'tweet': tweet}
            writer.writerow(new_row)

def main():
    open_Tweet_File()
    


if __name__ == "__main__" :
    #calling main function 
    main()