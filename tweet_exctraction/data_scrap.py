import tweepy
import csv

consumer_key = 'dtkROf4iX0xZzWeoLoIsycPBt'
consumer_secret = '251SRrsfuclGedVVhB7kFBuBgLtZOGSAXjpFdPW9U6L0eNNqHz'
access_token = '840985005203509248-pLbbZ6pa8RGuzO47cDHP4mpLKLLR9pR'
access_token_secret = '0rZViNGacrAb9MqWbxK6IZSdnLjk9azlWEHb2LhjPD1Pm'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('hashtagdataset.csv', 'a')
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="@RajkummarRao",count=200,
                           lang="en",
                           since="2018-09-06").items():


    import re
    from textblob import TextBlob

    try :        
        tweet_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    except:
        tweet_n = ['this', 'is', 'beautiful', 'sentence']

    tw = ' '
    for i in tweet_n:
        tw = tw + ' ' + i 

    analysis = TextBlob(tw)

    if analysis.sentiment.polarity > 0:
        value = 'positive'
    elif analysis.sentiment.polarity == 0:
        value = 'neutral'
    else:
        value = 'negative'

    print (tweet.created_at, tweet.text, value)
    csvWriter.writerow([tweet.created_at, tweet.text, value])