# https://realpython.com/twitter-bot-python-tweepy/#the-reply-to-mentions-bot

#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import sys
sys.path.append('../what-sentiment-bot/')
from bots.config import create_api
from ml.naive_bayes.predict import predict
from bots.utils.email_utils import email_error_report
import time
import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, since_id):
    
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        text = ""

        new_since_id = max(tweet.id, new_since_id)
        with open("bots/reply/since_id.txt", "w") as f:
            f.write('%d' % new_since_id)

        #if it has a father, reply to the father
        if tweet.in_reply_to_status_id is not None:
            logger.info(f"user that tagged: {tweet.user.name}")
            
            try:
                text = api.get_status(id = tweet.in_reply_to_status_id).text
            except tweepy.TweepError as error:
                if error.api_code in [179, 144]:
                    logger.info('not authorized or unexisting id')
                    email_error_report("not authorized or unexisting id, code 179 & 144")
                    continue
                else:
                    email_error_report(error)
        else:
            text = tweet.text

        probability, sentiment = predict(text)
        text = "That sounds like a "+ sentiment +" tweet"

        logger.info(f"user: {tweet.user.name}")
        logger.info(f"the tweet: {tweet.text}")

        try:
            api.update_status(
                status=text,
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )
        except tweepy.TweepError as error:
            if error.api_code == 187:
                logger.info('duplicate message')
                email_error_report('duplicate message, code 187')
            else:
                email_error_report(error)
    logger.info("")
    print()
    return new_since_id

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    f = open("bots/reply/since_id.txt", "r")
    since_id = int(f.readline())
    f.close()
    while True:
        since_id = check_mentions(api, since_id)
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(15)


if __name__ == "__main__":
    main()

