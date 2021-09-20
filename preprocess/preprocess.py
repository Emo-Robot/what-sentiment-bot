#responsable for 

import nltk                                # Python library for NLP
from nltk.corpus import twitter_samples    # sample Twitter dataset from NLTK
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

import re                                  # library for regular expression operations
import string                              # for string operations
import numpy as np

#removing undesired substrigns
def preprocess_tweet(tweet):
    stemmer = PorterStemmer()
    nltk.download('stopwords')
    stopwords_en = stopwords.words('english')

    print('\033[92m' + tweet)

    #remove stock market tickers, old rt, hyperlinks, hash sign 
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    tweet = re.sub(r'#','',tweet)

    #tokenize
    #preserve_case => downcase everything
    #strip_handles => removes @s (user handles)
    #reduce_len => removes repetitive letters
    tokenizer = TweetTokenizer(preserve_case=False,strip_handles=True,reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    
    #remove stopwords, ponctuation and perform steamming
    tweets_clean = []
    
    for word in tweet_tokens:
        if (word not in stopwords_en and word not in string.punctuation):
            stem_word = stemmer.stem(word)
            tweets_clean.append(stem_word)

    return tweets_clean