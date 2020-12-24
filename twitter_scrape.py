import tweepy as tw
import re, csv
import json
import textblob as tb


from tweepy import OAuthHandler
from datetime import datetime, timedelta
from flask import jsonify

from twitter_password import consumer_key, consumer_secret, access_token, access_secret

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tw.API(auth,wait_on_rate_limit=True)

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",txt).split())
    

def twitter(search_term,num):
    tweets = tw.Cursor(api.search,q=search_term,geo_enabled=True,lang="en").items(num)
    crimes = []
    for x in tweets:
        crime_inst = {'date':x._json["created_at"],'user':x._json["user"]['screen_name'],'img-url':x._json["user"]['profile_image_url_https'],'location':x._json["user"]['location'],'comment':x._json['text'],'no_retweets':x._json['retweet_count']}
        crimes.append(crime_inst)
    return crimes