# https://realpython.com/twitter-bot-python-tweepy/#the-reply-to-mentions-bot

#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py


import sys
sys.path.append('../what-sentiment-bot/')
from bots.config import create_api
import nltk
import time
import logging
from check_mention import check_mentions
from follow_follower import follow_followers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    #download necessary package data
    nltk.download('stopwords')
    #api
    api = create_api()
    #get since is
    f = open("bots/reply/since_id.txt", "r")
    since_id = int(f.readline())
    f.close()
    #run schedule
    count = 0
    while True:
        since_id = check_mentions(api, since_id)
        #run follow every 5 min
        if count == 5:
            follow_followers(api)
            count = 0
        logger.info("Waiting...")
        
        time.sleep(60)

        count = count+1



if __name__ == "__main__":
    main()

