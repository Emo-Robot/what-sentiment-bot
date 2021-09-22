from test_utils import get_random_tweet
from test_utils import get_dataset
import sys
sys.path.append('../what-sentiment-bot/')
from ml.naive_bayes.db.freqs_table.freqs_table import FreqsTable

get_dataset()

tweets = []
ys = []
#list of tweets
for i in range(50):
    tweets.append(get_random_tweet()[0])
    ys.append(get_random_tweet()[1])


table = FreqsTable.build_from(tweets, ys)

print(table.fetch_all_words())

