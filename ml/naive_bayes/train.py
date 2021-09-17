from db.freqs_table.freqs_table import FreqsTable
import sys
sys.path.append('../what-sentiment-bot/preprocess')
from preprocess import preprocess_tweet

freqs = FreqsTable()

freqs.create_words_freqs()
