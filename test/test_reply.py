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


api = create_api()

#tweet with the explicit mention @what_sentiment
tweet = api.get_status(1444125231258423301)
print(tweet.user_mentions)

#tweet without the excplicit mention
tweet = api.get_status(1444498192280731657)
print(tweet.user_mentions)
