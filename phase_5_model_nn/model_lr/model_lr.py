#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 01:10:52 2019

@author: gaurav
"""


from sklearn.feature_extraction.text import TfidfVectorizer
tvec1 = TfidfVectorizer(max_features=100000,ngram_range=(1, 3))
tvec1.fit(x_train)



x_train_tfidf = tvec1.transform(x_train)


x_validation_tfidf = tvec1.transform(x_validation).toarray()



from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(x_train_tfidf, y_train)


clf.score(x_validation_tfidf, y_validation)



clf.score(x_train_tfidf, y_train)




# Save logistic regression model
import pickle
save_lr = '/home/weithts_logistic_regression.h5'
#clf.save_weights(save_lr)


# save the model to disk
#filename = 'finalized_model.sav'
pickle.dump(clf, open(save_lr, 'wb'))
 
# some time later...
 
# load the model from disk
#loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X_test, Y_test)
#print(result)









