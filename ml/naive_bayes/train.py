import numpy as np
import nltk
from nltk.corpus import twitter_samples  
from db.freqs_table.freqs_table import FreqsTable

#get tweets
nltk.download('twitter_samples')

corpora_root = 'C:/Users/felip/AppData/Roaming/nltk_data/corpora/twitter_samples/'

all_positive_tweets = twitter_samples.strings(corpora_root + 'positive_tweets.json')
all_negative_tweets = twitter_samples.strings(corpora_root + 'negative_tweets.json')

#put them togheter
tweets = all_negative_tweets + all_negative_tweets

#get ys
pos_size = len(all_positive_tweets)
neg_size = len(all_negative_tweets)
ys = np.append(np.ones(pos_size), np.zeros(neg_size))

#build freqs table database and the utils table
table = FreqsTable.build_from(tweets, ys)
table.create_utils()

########################### TRAIN #########################################
#number of unique words
#TODO V TA TROLL????
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
table.add_logprior(logprior)

#list of positive and negative frequency
freq_pos = table.get_column('pos_freq')
freq_neg = table.get_column('neg_freq')
list_words = table.get_column('word')

#probability of each word being positive or negative
for freq_p, freq_n in zip(freq_pos, freq_neg):
    p_w_pos = (freq_p + 1) / (N_pos + V)
    p_w_neg = (freq_n + 1) / (N_neg + V)

#calculate loglikelihood
for word in list_words:
    log_likelihood= np.log(p_w_pos / p_w_neg)
    table.update_loglikelihood(log_likelihood, word)
