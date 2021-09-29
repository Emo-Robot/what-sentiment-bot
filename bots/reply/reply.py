# https://realpython.com/twitter-bot-python-tweepy/#the-reply-to-mentions-bot

#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import sys
sys.path.append('../what-sentiment-bot/bots')
import time
import datetime
from config import create_api
import tweepy
import logging
import pytz
from email.utils import parsedate_tz, mktime_tz

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#TODO se o usuario seguir o bot, o bot tem q seguir de volta

def check_mentions(api, since_id):
    
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        text = "aaaaaaaaaaa"

        new_since_id = max(tweet.id, new_since_id)

        if tweet.in_reply_to_status_id is not None:
            logger.info(f"user that tagged: {tweet.user.name}")
            
            try:
                text = api.get_status(id = tweet.in_reply_to_status_id).text
            except tweepy.TweepError as error:
                if error.api_code in [179, 144]:
                    continue
                else:
                    raise error

            text = "Test simple reply to father"
        else:
            text = "Test simple reply"

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
                print('duplicate message')
            else:
                raise error
    print()
    print()
    return new_since_id


def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(15)


if __name__ == "__main__":
    main()

