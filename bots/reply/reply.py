# https://realpython.com/twitter-bot-python-tweepy/#the-reply-to-mentions-bot


#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
import sys
sys.path.append('../what-sentiment-bot/bots')

from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        else:
            logger.info(f"Answering to {tweet.user.name}")

            api.update_status(
                status="Test simple reply",
                in_reply_to_status_id=tweet.id,
            )
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
