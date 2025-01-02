import sqlite3

CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

class Museum:
    pass

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS 
        """