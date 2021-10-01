import sys
sys.path.append('../what-sentiment-bot/')
from ml.preprocess import preprocess_tweet

from test_utils import *
import test_utils as test

get_dataset()

tweet = get_random_tweet()
#print('\033[92m' + tweet)

tweet = preprocess_tweet(tweet)
#print('\033[94m')
print(tweet)