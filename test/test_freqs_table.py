import numpy as np
from test_utils import get_random_tweet
from test_utils import get_dataset
import sys
sys.path.append('../what-sentiment-bot/')
from ml.naive_bayes.db.freqs_table.freqs_table import FreqsTable

get_dataset()

tweets = []
ys = []

#list of tweets
for i in range(5):
    tweet = get_random_tweet()
    tweets.append(tweet[0])
    ys.append(tweet[1])
    print(tweet[0] + "\n")


table = FreqsTable.build_from(tweets, ys)

print(table.fetch_all_words())

########################### TRAIN #########################################
#number of unique words
V = table.count_words()
print("V",V)
#sum of freqs of positive and negative words' columns
N_pos = table.sum_column('pos_freq')
N_neg = table.sum_column('neg_freq')
print("N_pos",N_pos)
print("N_neg",N_neg)

#number of documents
D = len(ys)
print("D",D)
#number of positive and negative docs
D_pos = sum(ys)
print("D_pos",D_pos)
D_neg = D - D_pos
print("D_neg",D_neg)

#reason between pos and neg docs
logprior = np.log(D_pos) - np.log(D_neg)
