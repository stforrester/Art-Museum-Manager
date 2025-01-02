from museum import CONN, CURSOR, Museum
from art import CONN, CURSOR, Art

asql = """
    DROP TABLE IF EXISTS art_collection
"""
msql = """
    DROP TABLE IF EXISTS museums
"""
CURSOR.execute(asql)
CURSOR.execute(msql)

Art.create_table()

import ipdb