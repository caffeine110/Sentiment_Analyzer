# Sentimennt Analysis in Twitter

It is a deep Learning model in which we can analyse the sentiment of tweets on a particular topic whether it is positive or negative and its overall impact.

### Data Collection
    Traininng Dataset :
    Training Dataset is collected from the Kaggle - https://www.kaggle.com/kazanova/sentiment140

    Real Time Tweets :
    Real time tweets were collected using API provided by twitter.
    To get Twitter API - Create Twitter Developer Account and create a project.


### Exploratory Data Analysis
EDA - Exploratory Data Analysis :
    
    Dataset contains 1.6 million tweets
    Polarity of tweets ( 0:Negative 2:Neutral 4:Positive )
    No of Positive Tweets : 800000 = 50% ( from 0 to 799999 )
    No of Negative Tweets : 800000 = 50% ( from 799999 to 1.6 m)


### Data Preprocessing
Pandas, NLTK, and RE were used in preprocessing the tweets.

    url address(‘http:’pattern), twitter ID removing
    url address(‘www.'pattern) removing
    lower-case
    negation handling
    removing numbers and special characters
    tokenizing and joining


### FeatureExctraction

    TFIDF Vectorizer - https://en.wikipedia.org/wiki/Tf%E2%80%93idf
    Count Vectorizer
    N-grams :
    unigram: 80,000 & 90,000 features
    bigram: 70,000 features
    trigram: 80,000 features


### LSTM Model
LSTM Model was built using Keras high level API with a Tensorflow as a backend and trained over Exctracted Features.

    ANN with Tfidf vectorizer
    LSTM Model


### Model Evaluation
The LSTM Model is 85% accurate on test data.

    Accuracy Score = ( TP + TN ) / Total
    Precision - https://en.wikipedia.org/wiki/Information_retrieval#Precision
    Recall - https://en.wikipedia.org/wiki/Information_retrieval#Recall
    F1 score - 2 (Precision.Recall)/(Precision+Recall)