#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  Fri Aug  10 23:43:32 2018

@author : gaurav gahukar
        : caffeine110

"""

#importing required libraries
import sys
from time import time

#Set the working directory
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



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
