import nltk                                # Python library for NLP
from nltk.corpus import twitter_samples    # sample Twitter dataset from NLTK
import random                              # pseudo-random number generator

all_positive_tweets = []
all_negative_tweets = []

pos_size = 0
neg_size = 0

def get_dataset():
    global all_positive_tweets
    global all_negative_tweets
    global pos_size
    global neg_size

    nltk.download('twitter_samples')

    corpora_root = 'C:/Users/felip/AppData/Roaming/nltk_data/corpora/twitter_samples/'

    all_positive_tweets = twitter_samples.strings(corpora_root + 'positive_tweets.json')
    all_negative_tweets = twitter_samples.strings(corpora_root + 'negative_tweets.json')

    pos_size = len(all_positive_tweets)
    neg_size = len(all_negative_tweets)

def get_random_pos():
    return all_positive_tweets[random.randint(0,pos_size)]

def get_random_neg():
    return all_negative_tweets[random.randint(0,neg_size)]

def get_random_tweet():
    pos_neg = random.randint(0,1)
    if pos_neg == 0 :
        return (get_random_neg(),0)
    else:
        return (get_random_pos(),1)