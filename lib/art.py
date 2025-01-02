import sqlite3

CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

class Art:
    pass

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS art_collection
                id INTEGER PRIMARY KEY,
                title TEXT,
                value INTEGER,
                artist TEXT,
                Dimensions TEXT,
                museum_id INTEGER;
        """
        CURSOR.execute(sql)