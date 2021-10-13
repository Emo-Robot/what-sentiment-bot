import sys
sys.path.append('../what-sentiment-bot/')
from bots.config import create_api
from ml.naive_bayes.predict import predict
from bots.utils.email_utils import email_error_report
import nltk
import time
import tweepy
import logging

# python3 c:/Users/felip/Documents/GitHub/what-sentiment-bot/test/test_reply.py
#& c:/Users/felip/Documents/GitHub/what-sentiment-bot/venv/Scripts/python.exe c:/Users/felip/Documents/GitHub/what-sentiment-bot/test/test_reply.py

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_duplicated_mentions(tweet):
    mentions = tweet.entities["user_mentions"]
    count = 0
    for x in mentions:
        if x["screen_name"] == "what_sentiment":
            count +=1
    
    return count






