import sqlite3


class DuoDictionary:
    def __init__(self,
                 story_name,
                 sqlite3_filename='Duolingo-dictionary.db',
                 ):
        self.sqlite3_filename = sqlite3_filename
        self.table_name = story_name.replace('-', '_')
        self.db_conn = sqlite3.connect(self.sqlite3_filename)
        self.cursor = self.db_conn.cursor()
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, a TEXT, b TEXT)"
        print(sql)
        self.cursor.execute(sql)

    def find(self, word):
        sql = f"SELECT a,b from {self.table_name} WHERE a='{word}'"
        print(sql)
        self.cursor.execute(sql)
        pair = self.cursor.fetchall()
        return True if pair else False

    def pair(self, word):
        sql = f"SELECT a,b from {self.table_name} WHERE a='{word}' OR b='{word}'"
        print(sql)
        self.cursor.execute(sql)
        pair = self.cursor.fetchall()
        if pair:
            return pair[0][0] if pair[0][0] != word else pair[0][1]
        return None

    def append(self, a, b):
        if not self.pair(a) or not self.pair(b):
            sql = f"INSERT INTO {self.table_name} (a, b) VALUES ('{a}','{b}')"
            print(sql)
            self.cursor.execute(sql)
            self.db_conn.commit()
        else:
            print(f"{a} and/or {b} exist. Didnot append.")
