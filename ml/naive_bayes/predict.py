
from db.freqs_table.freqs_table import FreqsTable
import sys
sys.path.append('../what-sentiment-bot/preprocess')
from preprocess import preprocess_tweet

def predict(tweet):
    db = FreqsTable()
    
    words = preprocess_tweet(tweet)

    probability = 0

    probability += db.get_utils()[0]
    

    for word in words:
        loglikelihood = db.get_loglikelihood(word)
        probability += loglikelihood
        

    return probability

def main():
    tweet = 'i am sad'
    p = predict(tweet)
    print(p)

main()