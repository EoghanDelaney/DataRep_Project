import tweepy as tw
import re, csv
import json
import textblob as tb


from tweepy import OAuthHandler
from textblob import TextBlob
from datetime import datetime, timedelta
from flask import jsonify

from twitter_password import consumer_key, consumer_secret, access_token, access_secret



auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tw.API(auth,wait_on_rate_limit=True)

search_term = ["#crime"]


def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",txt).split())
    

def twitter(search_term, num):
    tweets = tw.Cursor(api.search,q=search_term,geo_enabled=True,lang="en").items(num)
    print(type(tweets))
    new_col = []
    for x in tweets:
        print("**** New Tweet *****")
        print(str(x.created_at))                                # Date
        print(str(TextBlob(remove_url(x.text))))                # Text
        print(str(TextBlob(remove_url(x.user.screen_name))))    # User
        #print(str(x.user.location))                             # Location
        #new_tweet = new_col.append[{"date":str(x.created_at)},
        #             {"text":str(TextBlob(remove_url(x.text)))},    
        #             {"user":str(TextBlob(remove_url(x.user.screen_name)))}]
    #return jsonify(new_tweet)


twitter(search_term, 1)