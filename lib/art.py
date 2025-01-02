import sqlite3

CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

class Art:
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS art_collection
                (id INTEGER PRIMARY KEY,
                title TEXT,
                value INTEGER,
                artist TEXT,
                dimensions TEXT,
                museum_id INTEGER);
        """
        CURSOR.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS art_collection
        """
        CURSOR.execute(sql)
    
    @classmethod
    def create(cls, title, value, artist, dimensions):
        art = cls(title, value, artist, dimensions)
        art.save()
        return art

    @classmethod
    def instance_from_db(cls, row):
        art = cls(
            id=row[0],
            title=row[1],
            value=row[2],
            artist=row[3],
            dimensions=row[4],            
        )
        return art

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM art_collection;
        """
        return[cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    def __init__(self, title, value, artist, dimensions, id=None):
        self.id = id # primary key
        self.title = title
        self.value = value
        self.artist = artist
        self.dimensions = dimensions
        # self.museum_id = museum_id # foreign key
    
    def save(self):
        sql = """
            INSERT INTO art_collection (title, value, artist, dimensions)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql,(self.title, self.value, self.artist, self.dimensions))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    def __repr__(self):
        return f"<Artwork {self.id} {self.title} | {self.artist}>"