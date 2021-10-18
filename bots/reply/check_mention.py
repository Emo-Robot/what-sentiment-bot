import sys
sys.path.append('../what-sentiment-bot/')
from bots.reply.db.dynamo_db import *
from ml.naive_bayes.predict import predict
from bots.utils.email_utils import email_error_report
import tweepy
import logging
from check_duplicate_metion import check_duplicated_mentions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, since_id):
    
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        the_tweet = tweet

        #update id on db
        new_since_id = max(tweet.id, new_since_id)
        put_since_id(new_since_id)

        #if it has a father, reply to the father
        if tweet.in_reply_to_status_id is not None and check_duplicated_mentions(api.get_status(id = tweet.in_reply_to_status_id)) == 0:
            
            logger.info(f"user that tagged: {tweet.user.name}")
            
            try:
                the_tweet = api.get_status(id = tweet.in_reply_to_status_id)
            except tweepy.TweepError as error:
                if error.api_code in [179, 144]:
                    logger.info('not authorized or unexisting id')
                    email_error_report("not authorized or unexisting id, code 179 & 144")
                    continue
                else:
                    email_error_report(error)

        elif tweet.in_reply_to_status_id is not None and check_duplicated_mentions(api.get_status(id = tweet.in_reply_to_status_id)) >= 1:
            
            if check_duplicated_mentions(tweet) >= 2:
                logger.info(f"user that tagged: {tweet.user.name}")
            
                try:
                    the_tweet = api.get_status(id = tweet.in_reply_to_status_id)
                except tweepy.TweepError as error:
                    if error.api_code in [179, 144]:
                        logger.info('not authorized or unexisting id')
                        email_error_report("not authorized or unexisting id, code 179 & 144")
                        continue
                    else:
                        email_error_report(error)
            else:
                continue

        #predict
        probability, sentiment = predict(the_tweet.text)
        
        #if no words where recognized probably its not english
        if probability == 0:
            the_reply = "Sorry we don't recognize your language "
        else:
            the_reply = "That sounds like a "+ sentiment +" tweet"

        logger.info(f"user: {the_tweet.user.name}")
        logger.info(f"the tweet: {the_tweet.text}")
        logger.info(f"the probability: {probability}")
        logger.info(f"the reply: {the_reply}")

        try:
            api.update_status(
                status=the_reply,
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