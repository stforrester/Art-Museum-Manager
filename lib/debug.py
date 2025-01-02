from museum import CONN, CURSOR, Museum
from art import CONN, CURSOR, Art

msql = """
    DROP TABLE IF EXISTS museums
"""

Art.drop_table()

CURSOR.execute(msql)

Art.create_table()
artwork_1 = Art.create("The Scream", 119922500, "Edvard Munch", "36 in × 28.9 in")
artwork_2 = Art.create("Saturn Devouring His Son", 4500000, "Francisco Goya", "56.5 in × 32.0 in")

import ipdb

ipdb.set_trace()