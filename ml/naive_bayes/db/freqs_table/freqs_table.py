import sqlite3
import sqlite3
import os.path


class FreqsTable():

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

    ########################### CREATION ##################################
    def create_words_freqs(self):
        conn, cur = self.__connect_bd(self)

        # create words table
        cur.execute("""
            CREATE TABLE words (
                word text,
                sentiment integer,
                freq_id integer
            )
        """)
        # create freqs table
        cur.execute("""
            CREATE TABLE freqs (
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
