import sys
sys.path.append('../what-sentiment-bot/preprocess')
from preprocess import preprocess_tweet
import sqlite3
import os.path

filepath = os.path.abspath("ml/naive_bayes/db/freqs.db")
conn = sqlite3.connect(filepath)