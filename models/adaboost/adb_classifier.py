# -*- coding: utf-8 -*-
"""
Spyder Editor

aim : to build ann
date :18/6/18

"""
#importing the libraries

#importing required libraries
import pandas as pd
import numpy as np
import sys

#importing sklern library fucntions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif



#### Part - 1 : read dataset
#importing datasets
dataset = pd.read_csv('labeled_dataset/clean_tweet/final.csv')
# trial

X = dataset.iloc[:,1:1].values
Y = dataset.iloc[:,0:1].values

l = len(Y)

for i in range(0,l):
    if Y[i] == 4:
        Y[i]=1



#### Part - 2  : test train split

#spliting the data into the training and test datasets
from sklearn import cross_validation

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X,Y,test_size = 0.25, random_state = 0)


### Part - 3 : Vectorize

### text vectorization--go from strings to lists of numbers
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test  = vectorizer.transform(X_test)


### feature selection, because text is super high dimensional and 
### can be really computationally chewy as a result
selector = SelectPercentile(f_classif, percentile=10)
selector.fit(X_train, Y_train)
X_train = selector.transform(X_train).toarray()
X_test = selector.transform(X_test).toarray()


### info on the data
print("no. of Chris training emails: {} ".format(sum(Y_train)))
print("no. of Sara training emails: {} ".format(len(Y_train)-sum(Y_train)))






#import Classifier
from sklearn.ensemble import AdaBoostClassifier

#initialising classifier
ada_classifier = AdaBoostClassifier(n_estimators=50, learning_rate=1, random_state=0)

#fitting data to the classifer
ada_classifier.fit(features_train, labels_train)



from sklearn.metrics import accuracy_score
#prediction
author_pred = ada_classifier.predict(features_test)


#printing the accuracy
print(accuracy_score(labels_test, author_pred))
print(ada_classifier.score(features_test, labels_test))
