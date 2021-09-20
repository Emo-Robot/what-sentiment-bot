from preprocess.preprocess import preprocess_tweet
import numpy as np
import sqlite3
import sqlite3
import os.path


class FreqsTable():
    ######################### CONSTRUCTORS ################################

    #table = FreqsTable(tweets,ys)
    @classmethod
    def abacate(cls, tweets, ys):
        # create db
        conn, cur = cls.__connect_bd(cls)

        # create class
        table = cls.__new__(cls)  # Does not call __init__
        # Don't forget to call any polymorphic base class initializers
        super(FreqsTable, table).__init__()

        # np array to list
        yslist = np.squeeze(ys).tolist()

        # builds frequences dict by looping all tweets words
        freqs = {}

        for y, tweet in zip(yslist, tweets):
            for word in preprocess_tweet(tweet):
                pair = (word, y)
                if pair in freqs:
                    freqs[pair] += 1

                else:
                    cur.execute(
                        "INSERT INTO freqs VALUES (0, 0, 0.0)")
                    cur.execute(
                        "INSERT INTO words VALUES ({word}, {y}, {cur.lastrowid})")

        # close db
        cls.__disconnect(conn)

        # return class
        return table

    ########################### CONNECTION ##################################
    def __connect_bd(self):
        # create words table
        freqs_path = os.path.abspath("ml/naive_bayes/db/freqs_table/bd.db")
        # connect to db
        conn = sqlite3.connect(freqs_path)
        # create  cursor
        cur = conn.cursor()
        return conn, cur

    def __disconnect(self, conn):
        conn.commit()
        conn.close()

    ########################### CRUD ##################################
    def create_words_freqs(self):
        conn, cur = self.__connect_bd(self)

        # create word freqs table
        cur.execute("""
            CREATE TABLE words (
                word text,
                pos_freq integer,
                neg_freq integer,
                loglikelihood real
            )
        """)

        self.__disconnect(conn)

    def add_word(self, word: str, sentiment: int, pos_freq: int, neg_freq: int, loglikelihood: float):
        conn, cur = self.__connect_bd(self)

        cur.execute(
            "INSERT INTO freqs VALUES ({pos_freq},{neg_freq},{loglikelihood})")
        cur.execute(
            "INSERT INTO words VALUES ({word}, {sentiment}, {cur.lastrowid})")

        self.__disconnect(conn)

    # def add_word_set(self, word: str, sentiment: int, pos_freq: int, neg_freq: int):
    #     conn, cur = self.__connect_bd(self)

    #     ratio = pos_freq/neg_freq

    #     cur.execute("INSERT INTO freqs VALUES ({pos_freq},{neg_freq},{ratio})")
    #     cur.execute(
    #         "INSERT INTO words VALUES ({word}, {sentiment}, {freqs_cur.lastrowid})")

    #     self.__disconnect(conn)
