import sqlite3
import sqlite3
import os.path


class FreqsTable():

    ########################### CONNECTION ##################################
    def __connect_words(self):
        # create words table
        freqs_path = os.path.abspath("ml/naive_bayes/db/freqs_table/words.db")
        # connect to db
        conn = sqlite3.connect(freqs_path)
        # create  cursor
        cur = conn.cursor()
        return conn, cur

    def __connect_freqs(self):
        # create words table
        freqs_path = os.path.abspath("ml/naive_bayes/db/freqs_table/freqs.db")
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
        # create words table
        conn, cur = self.__connect_words()

        cur.execute("""
            CREATE TABLE words (
                word text,
                sentiment integer,
                freq_id integer
            )
        """)

        self.__disconnect(conn)

        # create freqs table
        conn, cur = self.__connect_freqs()

        cur.execute("""
            CREATE TABLE freqs (
                pos_freq integer,
                neg_freq integer,
                ratio real
            )
        """)

        self.__disconnect(conn)

    ########################### CRUD ##################################
    def add_word(self, word: str, sentiment: int, pos_freq:int, neg_freq:int):
        word_cur, word_conn = self.__connect_words()
        freqs_cur, freqs_conn = self.__connect_words()
        
        ratio = pos_freq/neg_freq

        freqs_cur.execute("INSERT INTO freqs VALUES ({pos_freq},{neg_freq},{ratio})")
        word_cur.execute("INSERT INTO words VALUES ({word}, {sentiment}, {freqs_cur.lastrowid})")

        self.__disconnect(freqs_conn)
        self.__disconnect(word_conn)
    
    def add_word_set(self, word: str, sentiment: int, pos_freq:int, neg_freq:int):
        word_cur, word_conn = self.__connect_words()
        freqs_cur, freqs_conn = self.__connect_words()
        
        ratio = pos_freq/neg_freq

        freqs_cur.execute("INSERT INTO freqs VALUES ({pos_freq},{neg_freq},{ratio})")
        word_cur.execute("INSERT INTO words VALUES ({word}, {sentiment}, {freqs_cur.lastrowid})")

        self.__disconnect(freqs_conn)
        self.__disconnect(word_conn)
