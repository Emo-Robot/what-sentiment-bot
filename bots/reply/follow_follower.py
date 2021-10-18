import sys
sys.path.append('../what-sentiment-bot/')
from bots.config import create_api
from ml.naive_bayes.predict import predict
from bots.utils.email_utils import email_error_report
import nltk
import time
import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


#TODO: Save list of users already asked to follow
def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                logger.info(f"Following {follower.name}")
                follower.follow()
            except tweepy.TweepError as error:
                if error.api_code == 160:
                    continue
                else:
                    logger.info("code \n" + str(error.api_code) +"reason \n" + error.reason + "cause \n" + error.__cause__)
                    email_error_report(error)