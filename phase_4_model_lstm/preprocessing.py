#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:25:39 2019

@author: gaurav
"""


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences




##########################################################################################
data = pd.read_csv('../phase_3_cleaning/cleaned_sentiment_tweet.csv')
# Keeping only the neccessary columns
data = data[['sentiment_value','tweet']]

#print(type(data))
print(data.columns)
#print(data.head(10))



##########################################################################################
#data = data[data.sentiment != "Neutral"]
#data['tweet'] = data['tweet'].apply(lambda x: x.lower())
#data['tweet'] = data['tweet'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

print(data.head(10))

print(data[ data['sentiment_value'] == 1].size)
print(data[ data['sentiment_value'] == 0].size)

data = data.dropna()

print(data[ data['sentiment_value'] == 1].size)
print(data[ data['sentiment_value'] == 0].size)


"""
for idx,row in data.iterrows():
    row[0] = row[0].replace('rt',' ')
"""

max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(data['tweet'].values)
X = tokenizer.texts_to_sequences(data['tweet'].values)
X = pad_sequences(X)

type(X)






from sklearn.model_selection import train_test_split

##########################################################################################
Y = pd.get_dummies(data['sentiment_value']).values
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)


