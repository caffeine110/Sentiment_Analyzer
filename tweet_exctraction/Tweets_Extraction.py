#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:38:27 2018

@author: Gaurav Gahukar

Aim : To Get Tweets form Twitter using provided API keys.

"""

#Step - 1 : Importing Libraries
import tweepy
import csv
import pandas as pd


# Step - 2 : Fill and Store The credentials provided by Twitter using Developer Accound
# input your credentials here

# keys
consumer_key = ''
consumer_secret = ''

# access tokens
access_token = ''
access_token_secret = ''


# step - 3 : User Authontication
# Authontication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


# Step - 4 : Open CSV file and Append the new data
# Open/Create a file to append data
csvFile = open('dataset.csv', 'a')

# Use csv Writer
csvWriter = csv.writer(csvFile)

# Step - 5 : Fill the Details about data tu be Extract
# eg. for  : @narendramodi all tweets since form 1/1/18 .
# encoding : utf-8 .
for tweet in tweepy.Cursor(api.search, q="@narendramodi", count=100, lang="en", since="2018-01-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
