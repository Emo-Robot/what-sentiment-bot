import sys
sys.path.append('../what-sentiment-bot/')
from ml.naive_bayes.predict import predict


def test():
    tweet = "negativo"
    probability, sentiment = predict(tweet)
    print(probability, sentiment)

test()